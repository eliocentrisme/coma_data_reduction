# phaseshift(vis='coma_lbandD0330.ms', outputvis='coma_lbandD0330_shifted.ms', phasecenter='J2000 12:54:11.712400 +27.37.30.465000')
# singularity exec ~/privatemodules/flocs_v5.6.0_sandybridge_sandybridge.sif wsclean -size 5000 5000 -scale 2asec -data-column DATA -update-model-required -reorder -weight briggs -0.5 -clean-border 1 -parallel-reordering 4 -gain 0.1 -mgain 0.7 -nmiter 30 -padding 1.4 -join-channels -channels-out 16 -local-rms -local-rms-strength 0.5 -auto-mask 3.0 -auto-threshold 0.5 -multiscale -multiscale-scale-bias 0.8 -multiscale-max-scales 7 -fit-spectral-pol 3 -pol i -gridder wgridder -fit-beam -name selfcal_images/shifted_selfcal_cycle_0 -niter 300000 coma_lbandD0330_shifted.ms > wsclean_shifted.log

import os
import subprocess

# change name of files and images, and solution intervales as needed

msfile = 'coma_lbandD0330_shifted2.ms' 
last_image = 'shifted2_last'
singularity_image = '~/privatemodules/flocs_v5.6.0_sandybridge_sandybridge.sif'


# solution_intervals = ['300s', '200s', '100s', '80s', '60s']
# solution_type = ['G', 'G', 'G', 'G', 'G']
# solution_mode = ['p', 'p', 'p', 'p', 'p']

solution_intervals = ['100s', '80s', '60s']
solution_type = ['G', 'G', 'G']
solution_mode = ['p', 'p', 'p']

last_ptable = f'selfcal/shifted2_gains_cycle_9.cal'
gain_solutions = []

wsclean_cmd = f"singularity exec {singularity_image} wsclean -size 5000 5000 -scale 2asec -data-column DATA -update-model-required -reorder -weight briggs -0.5 -clean-border 1 -parallel-reordering 4 -gain 0.1 -mgain 0.7 -nmiter 30 -padding 1.4 -join-channels -channels-out 16 -local-rms -local-rms-strength 0.5 -auto-mask 3.0 -auto-threshold 0.5 -multiscale -multiscale-scale-bias 0.8 -multiscale-max-scales 7 -fit-spectral-pol 3 -pol i -gridder wgridder -fit-beam -name selfcal_images/shifted_last -niter 1000000 {msfile}"

os.system(wsclean_cmd)

gaincal(vis=msfile, caltable=f'selfcal/shifted_last.cal', solint='100s', refant='ea09', gaintype='G', calmode='p')

applycal(vis=msfile, gaintable=f'selfcal/shifted_last.cal', calwt=False)

for idx, solint in enumerate(solution_intervals):
    image_name = f'selfcal_images/shifted2_selfcal_cycle_{idx+5}'
    gain_table = f'selfcal/shifted2_gains_cycle_{idx+5}.cal'
    
    wsclean_cmd = f"singularity exec {singularity_image} wsclean -size 5000 5000 -scale 2asec -data-column CORRECTED_DATA -update-model-required -reorder -weight briggs 0.0 -clean-border 1 -parallel-reordering 4 -gain 0.1 -mgain 0.7 -nmiter 30 -padding 1.4 -join-channels -channels-out 16 -fits-mask selfcal_images/shifted_mask.mask.fits -multiscale -multiscale-scale-bias 0.8 -multiscale-max-scales 7 -fit-spectral-pol 3 -pol i -gridder wgridder -parallel-deconvolution 2000 -fit-beam -name {image_name} -niter 1000000 {msfile}"
    
    os.system(wsclean_cmd)
    
    current_gain_tables = []
    
    if solution_mode[idx]=='p':
	    gaincal(vis=msfile, caltable=gain_table, solint=solint, refant='ea09', gaintype=solution_type[idx], calmode=solution_mode[idx])
 
    # if solution_mode[idx]=='ap':
    #     gaincal(vis=msfile, caltable=gain_table, solint=solint, refant='ea09', gaintype=solution_type[idx], calmode=solution_mode[idx], gaintable=[last_ptable], solnorm=True)
        
    #     current_gain_tables.append(last_ptable)

    current_gain_tables.append(gain_table)

    # Apply calibration solutions to the MS
    applycal(vis=msfile, gaintable=current_gain_tables, calwt=False)

wsclean_cmd = f"singularity exec {singularity_image} wsclean -size 5000 5000 -scale 2asec -data-column CORRECTED_DATA -update-model-required -reorder -weight briggs 0.0 -clean-border 1 -parallel-reordering 4 -gain 0.1 -mgain 0.7 -nmiter 30 -padding 1.4 -join-channels -channels-out 16 -fits-mask selfcal_images/shifted_mask.mask.fits -multiscale -multiscale-scale-bias 0.8 -multiscale-max-scales 7 -fit-spectral-pol 3 -pol i -gridder wgridder -parallel-deconvolution 2000 -fit-beam -name selfcal_images/{last_image} -niter 300000 {msfile}"

os.system(wsclean_cmd)

# bandpass(vis=msfile, caltable='selfcal/gains_cycle_bp.cal', solint='inf', refant='ea09', minsnr=3.0, parang=False, gaintable=['selfcal/gains_cycle_9.cal', 'selfcal/gains_cycle_12.cal'], solnorm=True)

# applycal(vis=msfile, gaintable=['selfcal/gains_cycle_9.cal', 'selfcal/gains_cycle_12.cal','selfcal/gains_cycle_bp.cal'], calwt=False)
    
# wsclean_cmd = f"singularity exec {singularity_image} wsclean -size 5100 5100 -scale 2arcsec -data-column CORRECTED_DATA -no-update-model-required -beam-size 9arcsec -reorder -weight briggs 0.0 -clean-border 1 -parallel-reordering 4 -gain 0.1 -mgain 0.7 -nmiter 30  -padding 1.4 -join-channels -channels-out 16 -local-rms -local-rms-strength 0.5 -auto-mask 3.0 -auto-threshold 0.5 -parallel-deconvolution 2000 -multiscale -multiscale-scale-bias 0.8 -multiscale-max-scales 7 -fit-spectral-pol 3 -pol i -gridder wgridder -fit-beam -name {last_image} -niter 200000 {msfile}"

# os.system(wsclean_cmd)