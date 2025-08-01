# First image: "pip" is for pipeline -> was to differenciate from a first try at calibration without the VLA pipeline

singularity_image = '~/privatemodules/flocs_v5.6.0_sandybridge_sandybridge.sif'

singularity exec singularity_image wsclean -size 2048 2048 -scale 2arcsec -data-column DATA -reorder -weight briggs -0.5 -clean-border 1 -parallel-reordering 4 -gain 0.1 -mgain 0.7 -nmiter 30  -padding 1.4 -join-channels -channels-out 16 -auto-mask 3.0 -auto-threshold 0.5 -multiscale -multiscale-scale-bias 0.8 -multiscale-max-scales 7 -fit-spectral-pol 3 -pol i -gridder wgridder -fit-beam -name selfcal_images/coma_pip -niter 200000 coma_pipcorrected.ms

gaincal(vis='coma_pipcorrected.ms', caltable='selfcal/coma_pip.ScG0', solint='inf', refant='ea09', minsnr=3.0, gaintype='G', parang=False, calmode='p')

# plotms(vis='coma_pip.ScG0', xaxis='time',yaxis='phase', gridrows=1,gridcols=2,iteraxis='antenna',coloraxis='corr',plotrange=[-1,-1,-180,180])

applycal(vis='coma_pipcorrected.ms', gaintable=['selfcal/coma_pip.ScG0'], applymode='calflagstrict')

singularity exec singularity_image wsclean -size 2048 2048 -scale 2arcsec -data-column CORRECTED_DATA -reorder -weight briggs -0.5 -clean-border 1 -parallel-reordering 4 -gain 0.1 -mgain 0.7 -nmiter 30  -padding 1.4 -join-channels -channels-out 16 -auto-mask 3.0 -auto-threshold 0.5 -multiscale -multiscale-scale-bias 0.8 -multiscale-max-scales 7 -fit-spectral-pol 3 -pol i -gridder wgridder -fit-beam -name selfcal_images/coma_pip_sc1   -niter 200000 coma_pipcorrected.ms

gaincal(vis='coma_pipcorrected.ms', caltable='selfcal/coma_pip.ScG1', solint='300s', refant='ea09', minsnr=3.0, gaintype='G', parang=False, calmode='p')

# plotms(vis='coma_pip.ScG1', xaxis='time',yaxis='phase', gridrows=1,gridcols=2,iteraxis='antenna',coloraxis='corr',plotrange=[-1,-1,-180,180])

applycal(vis='coma_pipcorrected.ms', gaintable=['selfcal/coma_pip.ScG1'], applymode='calflagstrict')

singularity exec singularity_image wsclean -size 2048 2048 -scale 2arcsec -data-column CORRECTED_DATA -reorder -weight briggs -0.5 -clean-border 1 -parallel-reordering 4 -gain 0.1 -mgain 0.7 -nmiter 30  -padding 1.4 -join-channels -channels-out 16 -local-rms -auto-mask 3.0 -auto-threshold 0.5 -multiscale -multiscale-scale-bias 0.8 -multiscale-max-scales 7 -fit-spectral-pol 3 -pol i -gridder wgridder -fit-beam -name selfcal_images/coma_pip_sc2  -niter 200000 coma_pipcorrected.ms

gaincal(vis='coma_pipcorrected.ms', caltable='selfcal/coma_pip.ScG2', solint='200s', refant='ea09', minsnr=3.0, gaintype='G', parang=False, calmode='p')

# plotms(vis='coma_pip.ScG2', xaxis='time',yaxis='phase',iteraxis='antenna',coloraxis='corr',plotrange=[-1,-1,-180,180])

applycal(vis='coma_pipcorrected.ms', gaintable=['selfcal/coma_pip.ScG2'], applymode='calflagstrict')

singularity exec singularity_image wsclean -size 2048 2048 -scale 2arcsec -data-column CORRECTED_DATA -reorder -weight briggs -0.5 -clean-border 1 -parallel-reordering 4 -gain 0.1 -mgain 0.7 -nmiter 30  -padding 1.4 -join-channels -channels-out 16 -local-rms -auto-mask 3.0 -auto-threshold 0.5 -multiscale -multiscale-scale-bias 0.8 -multiscale-max-scales 7 -fit-spectral-pol 3 -pol i -gridder wgridder -fit-beam -name selfcal_images/coma_pip_sc3   -niter 500000 coma_pipcorrected.ms

gaincal(vis='coma_pipcorrected.ms', caltable='selfcal/coma_pip.ScG3', solint='100s', refant='ea09', minsnr=3.0, gaintype='G', parang=False, calmode='p')

# plotms(vis='coma_pip.ScG3', xaxis='time',yaxis='phase',iteraxis='antenna',coloraxis='corr',plotrange=[-1,-1,-180,180])

applycal(vis='coma_pipcorrected.ms', gaintable=['selfcal/coma_pip.ScG3'], applymode='calflagstrict')

singularity exec singularity_image wsclean -size 2048 2048 -scale 2arcsec -data-column CORRECTED_DATA -update-model-required -reorder -weight briggs -0.5 -clean-border 1 -parallel-reordering 4 -gain 0.1 -mgain 0.7 -nmiter 30  -padding 1.4 -join-channels -channels-out 16 -local-rms -auto-mask 2.0 -auto-threshold 0.5 -multiscale -multiscale-scale-bias 0.8 -multiscale-max-scales 7 -fit-spectral-pol 3 -pol i -gridder wgridder -fit-beam -name selfcal_images/coma_pip_sc4 -niter 500000 coma_pipcorrected.ms

gaincal(vis='coma_pipcorrected.ms', caltable='selfcal/coma_pip.ScG4', solint='80s', refant='ea09', minsnr=3.0, gaintype='G', parang=False, calmode='p')

# plotms(vis='coma_pip.ScG4', xaxis='time',yaxis='phase',iteraxis='antenna',coloraxis='corr',plotrange=[-1,-1,-180,180])

applycal(vis='coma_pipcorrected.ms', gaintable=['selfcal/coma_pip.ScG4'], applymode='calflagstrict')

singularity exec singularity_image wsclean -size 2048 2048 -scale 2arcsec -data-column CORRECTED_DATA -update-model-required -reorder -weight briggs -0.5 -clean-border 1 -parallel-reordering 4 -gain 0.1 -mgain 0.7 -nmiter 30  -padding 1.4 -join-channels -channels-out 16 -local-rms -auto-mask 2.0 -auto-threshold 0.5 -multiscale -multiscale-scale-bias 0.8 -multiscale-max-scales 7 -fit-spectral-pol 3 -pol i -gridder wgridder -fit-beam -name selfcal_images/coma_pip_sc5 -niter 500000 coma_pipcorrected.ms

gaincal(vis='coma_pipcorrected.ms', caltable='selfcal/coma_pip.ScG5', solint='60s', refant='ea09', minsnr=3.0, gaintype='G', parang=False, calmode='p')

# plotms(vis='coma_pip.ScG5', xaxis='time',yaxis='phase',iteraxis='antenna',coloraxis='corr',plotrange=[-1,-1,-180,180])

applycal(vis='coma_pipcorrected.ms', gaintable=['selfcal/coma_pip.ScG5'], applymode='calflagstrict')

singularity exec singularity_image wsclean -size 2048 2048 -scale 2arcsec -data-column CORRECTED_DATA -update-model-required -reorder -weight briggs -0.5 -clean-border 1 -parallel-reordering 4 -gain 0.1 -mgain 0.7 -nmiter 30  -padding 1.4 -join-channels -channels-out 16 -local-rms -auto-mask 2.0 -auto-threshold 0.5 -multiscale -multiscale-scale-bias 0.8 -multiscale-max-scales 7 -fit-spectral-pol 3 -pol i -gridder wgridder -fit-beam -name selfcal_images/coma_pip_sc6 -niter 100000 coma_pipcorrected.ms

gaincal(vis='coma_pipcorrected.ms', caltable='selfcal/coma_pip.ScG6', solint='40s', refant='ea09', minsnr=3.0, gaintype='G', parang=False, calmode='p')

# plotms(vis='coma_pip.ScG6', xaxis='time',yaxis='phase',iteraxis='antenna',coloraxis='corr',plotrange=[-1,-1,-180,180])

applycal(vis='coma_pipcorrected.ms', gaintable=['selfcal/coma_pip.ScG6'], applymode='calflagstrict')

singularity exec singularity_image wsclean -size 2048 2048 -scale 2arcsec -data-column CORRECTED_DATA -update-model-required -reorder -weight briggs -0.5 -clean-border 1 -parallel-reordering 4 -gain 0.1 -mgain 0.7 -nmiter 30  -padding 1.4 -join-channels -channels-out 16 -local-rms -auto-mask 1.5 -auto-threshold 0.3 -multiscale -multiscale-scale-bias 0.8 -multiscale-max-scales 7 -fit-spectral-pol 3 -pol i -gridder wgridder -fit-beam -name selfcal_images/coma_pip_sc7 -niter 400000 coma_pipcorrected.ms

gaincal(vis='coma_pipcorrected.ms', caltable='selfcal/coma_pip.ScG7', solint='20s', refant='ea09', minsnr=3.0, gaintype='G', parang=False, calmode='p')

# plotms(vis='coma_pip.ScG7', xaxis='time',yaxis='phase',iteraxis='antenna',coloraxis='corr',plotrange=[-1,-1,-180,180])

applycal(vis='coma_pipcorrected.ms', gaintable=['selfcal/coma_pip.ScG7'], applymode='calflagstrict')

singularity exec singularity_image wsclean -size 2048 2048 -scale 2arcsec -data-column CORRECTED_DATA -update-model-required -reorder -weight briggs -0.5 -clean-border 1 -parallel-reordering 4 -gain 0.1 -mgain 0.7 -nmiter 30  -padding 1.4 -join-channels -channels-out 16 -local-rms -auto-mask 2.0 -auto-threshold 0.3 -multiscale -multiscale-scale-bias 0.8 -multiscale-max-scales 7 -fit-spectral-pol 3 -pol i -gridder wgridder -fit-beam -name selfcal_images/coma_pip_sc8 -niter 200000 coma_pipcorrected.ms
# missing the tail from the model

gaincal(vis='coma_pipcorrected.ms', caltable='selfcal/coma_pip.ScG8', solint='10s', refant='ea09', minsnr=3.0, gaintype='G', parang=False, calmode='p')

# plotms(vis='coma_pip.ScG8', xaxis='time',yaxis='phase',iteraxis='antenna',coloraxis='corr',plotrange=[-1,-1,-180,180])

applycal(vis='coma_pipcorrected.ms', gaintable=['selfcal/coma_pip.ScG8'], applymode='calflagstrict')

# to make a mask: create image (importfits('coma_pip_sc8-MFS-image.fits','coma_pip_sc8.image')), create .crtf region file, make mask (makemask(mode='copy', inpmask='coma-mask.crtf', output='coma_pip_sc8.mask', inpimage='coma_pip_sc8.image'))

singularity exec singularity_image wsclean -size 2048 2048 -scale 2arcsec -data-column CORRECTED_DATA -update-model-required -reorder -weight briggs -0.5 -clean-border 1 -parallel-reordering 4 -gain 0.1 -mgain 0.7 -nmiter 30  -padding 1.4 -join-channels -channels-out 16 -local-rms -auto-mask 1.0 -auto-threshold 0.6 -multiscale -multiscale-scale-bias 0.8 -multiscale-max-scales 7 -fit-spectral-pol 3 -pol i -gridder wgridder -fit-beam -name selfcal_images/coma_pip_sc9 -niter 200000 coma_pipcorrected.ms

gaincal(vis='coma_pipcorrected.ms', caltable='selfcal/coma_pip.ScG9', solint='8s', refant='ea09', minsnr=3.0, gaintype='G', parang=False, calmode='p')

# plotms(vis='coma_pip.ScG9', xaxis='time',yaxis='phase',iteraxis='antenna',coloraxis='corr',plotrange=[-1,-1,-180,180])

applycal(vis='coma_pipcorrected.ms', gaintable=['selfcal/coma_pip.ScG9'], applymode='calflagstrict')

singularity exec singularity_image wsclean -size 2048 2048 -scale 2arcsec -data-column CORRECTED_DATA -update-model-required -reorder -weight briggs -0.5 -clean-border 1 -parallel-reordering 4 -gain 0.1 -mgain 0.7 -nmiter 30  -padding 1.4 -join-channels -channels-out 16 -fits-mask coma_pip_sc16-mask.mask.fits -multiscale -multiscale-scale-bias 0.8 -multiscale-max-scales 7 -fit-spectral-pol 3 -pol i -gridder wgridder -fit-beam -name selfcal_images/coma_pip_sc10 -niter 200000 coma_pipcorrected.ms

gaincal(vis='coma_pipcorrected.ms', caltable='selfcal/coma_pip.ScG10', solint='int', refant='ea09', minsnr=3.0, gaintype='G', parang=False, calmode='p')

# plotms(vis='coma_pip.ScG10', xaxis='time',yaxis='phase',iteraxis='antenna',coloraxis='corr',plotrange=[-1,-1,-180,180])

applycal(vis='coma_pipcorrected.ms', gaintable=['selfcal/coma_pip.ScG10'], applymode='calflagstrict')

# amplitude calibration
singularity exec singularity_image wsclean -size 3000 3000 -scale 2arcsec -data-column CORRECTED_DATA -update-model-required -reorder -weight briggs -0.5 -clean-border 1 -parallel-reordering 4 -gain 0.1 -mgain 0.7 -nmiter 30  -padding 1.4 -join-channels -channels-out 16 -fits-mask coma_pip_sc11-mask.mask.fits -multiscale -multiscale-scale-bias 0.8 -multiscale-max-scales 7 -fit-spectral-pol 3 -pol i -gridder wgridder -fit-beam -name selfcal_images/coma_pip_sc11-mask -niter 100000 coma_pipcorrected.ms

gaincal(vis='coma_pipcorrected.ms', caltable='selfcal/coma_pip.ScG11_amp', solint='inf', refant='ea09', minsnr=3.0, gaintype='G', parang=False, calmode='ap', gaintable='selfcal/coma_pip.ScG10',solnorm=True)

# plotms(vis='coma_pip.ScG11_amp', xaxis='time',yaxis='phase',iteraxis='antenna',coloraxis='corr',plotrange=[-1,-1,-180,180])

# plotms(vis='coma_pip.ScG11_amp', xaxis='time',yaxis='amp',iteraxis='antenna',coloraxis='corr',plotrange=[-1,-1,-180,180])

applycal(vis='coma_pipcorrected.ms', gaintable=['selfcal/coma_pip.ScG10', 'selfcal/coma_pip.ScG11_amp'], applymode='calflagstrict')

singularity exec singularity_image wsclean -size 3000 3000 -scale 2arcsec -data-column CORRECTED_DATA -update-model-required -reorder -weight briggs -0.5 -clean-border 1 -parallel-reordering 4 -gain 0.1 -mgain 0.7 -nmiter 30  -padding 1.4 -join-channels -channels-out 16 -fits-mask coma_pip_sc11-mask.mask.fits -multiscale -multiscale-scale-bias 0.8 -multiscale-max-scales 7 -fit-spectral-pol 3 -pol i -gridder wgridder -fit-beam -name selfcal_images/coma_pip_sc12 -niter 100000 coma_pipcorrected.ms

gaincal(vis='coma_pipcorrected.ms', caltable='selfcal/coma_pip.ScG12_amp', solint='300s', refant='ea09', minsnr=3.0, gaintype='G', parang=False, calmode='ap', gaintable='selfcal/coma_pip.ScG10',solnorm=True)

# plotms(vis='coma_pip.ScG12_amp', xaxis='time',yaxis='phase',iteraxis='antenna',coloraxis='corr',plotrange=[-1,-1,-180,180])

# plotms(vis='coma_pip.ScG12_amp', xaxis='time',yaxis='amp',iteraxis='antenna',coloraxis='corr',plotrange=[-1,-1,-180,180])

applycal(vis='coma_pipcorrected.ms', gaintable=['selfcal/coma_pip.ScG10', 'selfcal/coma_pip.ScG12_amp'], applymode='calflagstrict')

singularity exec singularity_image wsclean -size 3000 3000 -scale 2arcsec -data-column CORRECTED_DATA -update-model-required -reorder -weight briggs -0.5 -clean-border 1 -parallel-reordering 4 -gain 0.1 -mgain 0.7 -nmiter 30  -padding 1.4 -join-channels -channels-out 16 -fits-mask coma_pip_sc11-mask.mask.fits -multiscale -multiscale-scale-bias 0.8 -multiscale-max-scales 7 -fit-spectral-pol 3 -pol i -gridder wgridder -fit-beam -name selfcal_images/coma_pip_sc13 -niter 200000 coma_pipcorrected.ms

gaincal(vis='coma_pipcorrected.ms', caltable='selfcal/coma_pip.ScG13_amp', solint='200s', refant='ea09', minsnr=3.0, gaintype='G', parang=False, calmode='ap', gaintable='selfcal/coma_pip.ScG10',solnorm=True)

# plotms(vis='coma_pip.ScG13_amp', xaxis='time',yaxis='phase',iteraxis='antenna',coloraxis='corr',plotrange=[-1,-1,-180,180])

# plotms(vis='coma_pip.ScG13_amp', xaxis='time',yaxis='amp',iteraxis='antenna',coloraxis='corr',plotrange=[-1,-1,-180,180])

applycal(vis='coma_pipcorrected.ms', gaintable=['selfcal/coma_pip.ScG10', 'selfcal/coma_pip.ScG13_amp'], applymode='calflagstrict')

singularity exec singularity_image wsclean -size 3000 3000 -scale 2arcsec -data-column CORRECTED_DATA -update-model-required -reorder -weight briggs -0.5 -clean-border 1 -parallel-reordering 4 -gain 0.1 -mgain 0.7 -nmiter 30  -padding 1.4 -join-channels -channels-out 16 -fits-mask coma_pip_sc11-mask.mask.fits -multiscale -multiscale-scale-bias 0.8 -multiscale-max-scales 7 -fit-spectral-pol 3 -pol i -gridder wgridder -fit-beam -name selfcal_images/coma_pip_sc14 -niter 200000 coma_pipcorrected.ms

gaincal(vis='coma_pipcorrected.ms', caltable='selfcal/coma_pip.ScG14_amp', solint='60s', refant='ea09', minsnr=3.0, gaintype='G', parang=False, calmode='ap', gaintable='selfcal/coma_pip.ScG10',solnorm=True)

# plotms(vis='coma_pip.ScG14_amp', xaxis='time',yaxis='phase',iteraxis='antenna',coloraxis='corr',plotrange=[-1,-1,-180,180])

# plotms(vis='coma_pip.ScG14_amp', xaxis='time',yaxis='amp',iteraxis='antenna',coloraxis='corr',plotrange=[-1,-1,-180,180])

applycal(vis='coma_pipcorrected.ms', gaintable=['selfcal/coma_pip.ScG10', 'selfcal/coma_pip.ScG14_amp'], applymode='calflagstrict')

# bandpass calibration
singularity exec singularity_image wsclean -size 3000 3000 -scale 2arcsec -data-column CORRECTED_DATA -update-model-required -reorder -weight briggs -0.5 -clean-border 1 -parallel-reordering 4 -gain 0.1 -mgain 0.7 -nmiter 30  -padding 1.4 -join-channels -channels-out 16 -fits-mask coma_pip_sc11-mask.mask.fits -multiscale -multiscale-scale-bias 0.8 -multiscale-max-scales 7 -fit-spectral-pol 3 -pol i -gridder wgridder -fit-beam -name selfcal_images/coma_pip_sc15 -niter 200000 coma_pipcorrected.ms

bandpass(vis='coma_pipcorrected.ms', caltable='selfcal/coma_pip.ScG15_b', solint='inf', refant='ea09', minsnr=3.0, parang=False, gaintable=['selfcal/coma_pip.ScG10', 'selfcal/coma_pip.ScG14_amp'], solnorm=True)

# plotms(vis='coma_pip.ScG15_b', xaxis='freq',yaxis='amp',iteraxis='antenna',coloraxis='corr')

applycal(vis='coma_pipcorrected.ms', gaintable=['selfcal/coma_pip.ScG10', 'selfcal/coma_pip.ScG14_amp', 'selfcal/coma_pip.ScG15_b'], applymode='calflagstrict')

## baseline calibration DOESN'T IMPROVE IMAGE
singularity exec singularity_image wsclean -size 5100 5100 -scale 2arcsec -data-column CORRECTED_DATA -update-model-required -reorder -weight briggs -0.5 -clean-border 1 -parallel-reordering 4 -gain 0.1 -mgain 0.7 -nmiter 30  -padding 1.4 -join-channels -channels-out 16 -fits-mask selfcal_images/bp_mask.mask.fits -multiscale -multiscale-scale-bias 0.8 -multiscale-max-scales 7 -fit-spectral-pol 3 -pol i -gridder wgridder -fit-beam -parallel-deconvolution 2000 -name selfcal_images/selfcal_cycle_bp -niter 200000 coma_pipcorrected.ms > selfcal_images/wsclean_bp.log


# copy ms in case baseline calibration changes the data a lot
# cp -rf coma_pipcorrected.ms coma_lbandC1.ms

## baseline calibration
blcal(vis='coma_lbandC1.ms', caltable='selfcal/baseline.cal')

# plotms(vis='selfcal/baseline.cal', xaxis='freq',yaxis='amp',iteraxis='antenna',coloraxis='corr')

applycal(vis='coma_lbandC1.ms', gaintable=['selfcal/coma_pip.ScG10', 'selfcal/coma_pip.ScG14_amp', 'selfcal/coma_pip.ScG15_b', 'selfcal/baseline.cal'], applymode='calflagstrict')

singularity exec ~/privatemodules/flocs_v5.6.0_sandybridge_sandybridge.sif wsclean -size 5100 5100 -scale 2arcsec -beam-size 9arcsec -data-column CORRECTED_DATA -no-update-model-required -reorder -weight briggs -0.5 -clean-border 1 -parallel-reordering 4 -gain 0.1 -mgain 0.7 -nmiter 30  -padding 1.4 -join-channels -channels-out 16 -fits-mask selfcal_images/bp_mask.mask.fits -multiscale -multiscale-scale-bias 0.8 -multiscale-max-scales 7 -fit-spectral-pol 3 -pol i -gridder wgridder -fit-beam -parallel-deconvolution 2000 -name coma_lbandC0309_with_blcal -niter 300000 coma_lbandC1.ms > wsclean.log