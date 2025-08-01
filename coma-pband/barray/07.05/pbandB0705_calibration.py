from casatasks.private import tec_maps
name = 'coma_pbandC1'

listobs_file = listobs(vis=f'{name}.ms', verbose=True, listfile=f'{name}.listobs')

plotants(vis=f'{name}.ms', figfile=f'{name}_plotants.png')

plotms(vis=f'{name}.ms', xaxis='freq', yaxis='amp', antenna='ea02', correlation='XX,YY', field='3C286',  plotrange=[0.2,0.5,0.0,100.0], coloraxis='spw', xlabel='Frequency', ylabel='Amplitude', iteraxis='baseline')

flagdata(vis=f'{name}.ms', mode='manual', scan='1~2')

flagdata(vis=f'{name}.ms', mode='shadow', tolerance=0.0, flagbackup=False)

flagdata(vis=f'{name}.ms', mode='clip', clipzeros=True, flagbackup=False)

flagdata(vis=f'{name}.ms', mode='quack', quackinterval=5.0, quackmode='beg', flagbackup=False)

# cd calibration
os.system('cd calibration')

hanningsmooth(vis=f'../{name}.ms', outputvis=f'{name}_hanning.ms', datacolumn='data', spw='0~15')

# plotms(vis=f'{name}_hanning.ms', xaxis='freq', yaxis='amp', antenna='ea02', correlation='XX,YY', field='3C286', plotrange=[0.2,0.5,0.0,100.0], coloraxis='spw',iteraxis='baseline')

gencal(vis=f'{name}_hanning.ms', caltable=f'{name}_hanning.antpos', caltype='antpos')

tec_image, tec_rms_image, plotname = tec_maps.create(vis=f'{name}_hanning.ms', doplot=True)

gencal(vis=f'{name}_hanning.ms', caltable=f'{name}_hanning.tecim', caltype='tecim', infile=tec_image)

gencal(vis=f'{name}_hanning.ms', caltype='rq', caltable=f'{name}_hanning.rq')

# plotms(vis=f'{name}_hanning.ms',correlation='RR,LL',antenna='ea01',xaxis='freq',yaxis='amp',coloraxis='spw',iteraxis='baseline')

flagdata(vis=f'{name}_hanning.ms', field='*', mode='tfcrop', datacolumn='data', timecutoff=4., freqcutoff=3., maxnpieces=5, action='apply', display='report', flagbackup=True, combinescans=True, ntime='3600s', correlation='ABS_XY,ABS_YX')

flagdata(vis=f'{name}_hanning.ms', field='*', mode='tfcrop', datacolumn='data',timecutoff=3., freqcutoff=3., maxnpieces=2, action='apply', display='report', flagbackup=False, combinescans=True, ntime='3600s', correlation='ABS_XX,ABS_YY')

flagdata(vis=f'{name}_hanning.ms', mode='extend')

# plotms(vis=f'{name}_hanning.ms',xaxis='freq',yaxis='amp', ydatacolumn = 'corrected', antenna='ea02',correlation='XX,YY', field='3C286', plotrange=[0.2,0.5,0.0,100.0], coloraxis='spw', iteraxis='baseline')

# INTERACTIVE: choose good channels in each spw with this plot
plotms(vis=f'{name}_hanning.ms',antenna='ea02',xaxis='channel',yaxis='amp',iteraxis='spw')

spw_chan = '0:55~65,1:55~65,2:25~30,3:60~70,4:55~65,5:85~95,6:75~85,7:55~65,8:50~60,9:100~110,10:55~65,11:70~80,12:90~100,13:90~100,14:60~70,15:55~65'

gaincal(vis=f'{name}_hanning.ms', caltable=f'{name}_hanning.G0', gaintype='G', calmode='p', solint='int', field='3C286',refant='ea25', spw='0:55~65,1:55~65,2:25~30,3:60~70,4:55~65,5:85~95,6:75~85,7:55~65,8:50~60,9:100~110,10:55~65,11:70~80,12:90~100,13:90~100,14:60~70,15:55~65', gaintable=[f'{name}_hanning.antpos',f'{name}_hanning.rq',f'{name}_hanning.tecim'])

gaincal(vis=f'{name}_hanning.ms', caltable=f'{name}_hanning.K0', gaintype='K', solint='inf', field='3C286',refant='ea25', spw='0:55~65,1:55~65,2:25~30,3:60~70,4:55~65,5:85~95,6:75~85,7:55~65,8:50~60,9:100~110,10:55~65,11:70~80,12:90~100,13:90~100,14:60~70,15:55~65', gaintable=[f'{name}_hanning.antpos',f'{name}_hanning.rq',f'{name}_hanning.tecim',f'{name}_hanning.G0'])

bandpass(vis=f'{name}_hanning.ms', caltable=f'{name}_hanning.B0', solint='inf', field='3C286',refant='ea25', minsnr=2.0, gaintable=[f'{name}_hanning.antpos',f'{name}_hanning.rq',f'{name}_hanning.tecim',f'{name}_hanning.G0',f'{name}_hanning.K0'])

# INTERACTIVE: flag outliers
plotms(vis=f'{name}_hanning.B0', xaxis='freq', yaxis='amp', iteraxis='antenna', coloraxis='spw')

applycal(vis=f'{name}_hanning.ms', field='3C286', applymode='calflagstrict', gaintable=[f'{name}_hanning.antpos',f'{name}_hanning.rq',f'{name}_hanning.tecim',f'{name}_hanning.G0',f'{name}_hanning.K0',f'{name}_hanning.B0'] )

# plotms(vis=f'{name}_hanning.ms',xaxis='freq',yaxis='amp', ydatacolumn = 'corrected', antenna='ea01',correlation='XX,YY', field='3C286', plotrange=[0.2,0.5,0.0,100.0], coloraxis='spw', iteraxis='baseline')

flagdata(vis=f'{name}_hanning.ms', mode='rflag', field='3C286,J1330+2509', datacolumn='corrected', timedevscale=3., freqdevscale=3.,action='apply', display = 'report', flagbackup=False, combinescans=True, ntime='3600s')

flagdata(vis=f'{name}_hanning.ms', mode='rflag', field='3C286,J1330+2509', spw='15', datacolumn='corrected', timedevscale=2., freqdevscale=2.,action='apply', display = 'report', flagbackup=False, combinescans=True, ntime='3600s')

flagdata(vis=f'{name}_hanning.ms', mode='manual', spw='2,9', flagbackup=True)

# plotms(vis=f'{name}_hanning.ms',xaxis='freq',yaxis='amp',antenna='ea02',correlation='XX,YY', field='3C286', plotrange=[0.2,0.5,0.0,100.0], coloraxis='spw', iteraxis='baseline', ydatacolumn='corrected')

# plotms(vis=f'{name}_hanning.ms',xaxis='freq',yaxis='amp',antenna='ea02',correlation='XX,YY', field='J1330+2509', plotrange=[0.2,0.5,0.0,100.0], coloraxis='spw', iteraxis='baseline', ydatacolumn='data')

clearcal(vis=f'{name}_hanning.ms')

setjy(vis=f'{name}_hanning.ms', field='3C286', usescratch=True)

gaincal(vis=f'{name}_hanning.ms', caltable=f'{name}_hanning.K1', field='3C286', solint='inf', refant='ea27', gaintype='K', gaintable=[f'{name}_hanning.antpos',f'{name}_hanning.tecim',f'{name}_hanning.rq'])

plotms(vis=f'{name}_hanning.K1',xaxis='antenna1',yaxis='delay',plotrange=[0,30,-50.,50.])

bandpass(vis=f'{name}_hanning.ms', caltable=f'{name}_hanning.B1', field='3C286', solint='inf', refant='ea27', minsnr=3.0, parang = True, gaintable=[f'{name}_hanning.antpos',f'{name}_hanning.tecim',f'{name}_hanning.rq',f'{name}_hanning.K1'], interp=['','','','nearest,nearestflag'])

# INTERACTIVE: flag outliers
plotms(vis=f'{name}_hanning.B1', xaxis='freq', yaxis='amp', iteraxis='antenna', coloraxis='spw')

plotms(vis=f'{name}_hanning.B1', xaxis='freq', yaxis='phase', iteraxis='antenna', plotrange=[0,0,-180.,180.], coloraxis='spw')

gaincal(vis=f'{name}_hanning.ms', caltable=f'{name}_hanning.G1', field='3C286,J1330+2509', solint='int', refant='ea27', minsnr=3.0, gaintype='G', calmode='ap', gaintable=[f'{name}_hanning.antpos',f'{name}_hanning.rq',f'{name}_hanning.tecim',f'{name}_hanning.K1',f'{name}_hanning.B1'], interp=['','','','nearest,nearestflag','nearest,nearestflag'])

# plotms(vis=f'{name}_hanning.G1', xaxis='time', yaxis='amp', iteraxis='antenna', coloraxis='spw')

# plotms(vis=f'{name}_hanning.G1', xaxis='time', yaxis='phase', plotrange=[0,0,-180.,180.], iteraxis='corr', coloraxis='baseline')

# plotms(vis=f'{name}_hanning.G1', xaxis='time', yaxis='phase', correlation='/', coloraxis='baseline', plotrange=[-1,-1,-180,180])


myscale = fluxscale(vis=f'{name}_hanning.ms', caltable=f'{name}_hanning.G1', fluxtable=f'{name}_hanning.fluxscale1', reference='3C286', transfer=['J1330+2509'], incremental=False)

applycal(vis=f'{name}_hanning.ms', field='3C286', parang=True, applymode='calflagstrict', flagbackup=True, gaintable=[f'{name}_hanning.antpos',f'{name}_hanning.rq',f'{name}_hanning.tecim',f'{name}_hanning.K1',f'{name}_hanning.B1',f'{name}_hanning.G1', f'{name}_hanning.fluxscale1'], gainfield=['', '', '', '', '', '', '3C286'], interp=['','','','nearest,nearestflag','nearest,nearestflag','nearest,nearestflag', 'nearest'])

applycal(vis=f'{name}_hanning.ms', field='J1330+2509', parang=True, applymode='calflagstrict', flagbackup=True, gaintable=[f'{name}_hanning.antpos',f'{name}_hanning.rq',f'{name}_hanning.tecim',f'{name}_hanning.K1',f'{name}_hanning.B1',f'{name}_hanning.G1', f'{name}_hanning.fluxscale1'], gainfield=['', '', '', '', '', '', 'J1330+2509'], interp=['','','','nearest,nearestflag','nearest,nearestflag','nearest,nearestflag', 'nearest'])

applycal(vis=f'{name}_hanning.ms', field='NGC4869', parang=True, applymode='calflagstrict', flagbackup=True, gaintable=[f'{name}_hanning.antpos',f'{name}_hanning.rq',f'{name}_hanning.tecim',f'{name}_hanning.K1',f'{name}_hanning.B1',f'{name}_hanning.G1', f'{name}_hanning.fluxscale1'], gainfield=['', '', '', '', '', '', 'J1330+2509'], interp=['','','','nearest,nearestflag','nearest,nearestflag','nearest,nearestflag', 'linear'])

split(vis=f'{name}_hanning.ms', outputvis=f'../coma_{name}_hanning.ms', datacolumn='corrected', field='NGC4869')

flagdata(vis=f'coma_{name}_hanning.ms', mode='rflag')

flagdata(vis=f'coma_{name}_hanning.ms', mode='extend')

statwt(vis=f'coma_{name}_hanning.ms', datacolumn='data', timebin=30)

################################################################
###################### SELF-CALIBRATION ########################
################################################################

singularity_image = '~/privatemodules/flocs_v5.6.0_sandybridge_sandybridge.sif'

singularity exec singularity_image wsclean -size 5000 5000 -scale 2.5asec -data-column DATA -update-model-required -reorder -weight briggs -0.5 -clean-border 1 -parallel-reordering 4 -gain 0.1 -mgain 0.7 -nmiter 30  -padding 1.4 -join-channels -channels-out 16 -local-rms -local-rms-strength 0.5 -auto-mask 3.0 -auto-threshold 0.5 -multiscale -multiscale-scale-bias 0.8 -multiscale-max-scales 7 -fit-spectral-pol 3 -pol i -gridder wgridder -fit-beam -dd-psf-grid 6 6 -parallel-deconvolution 2000 -name selfcal_images/selfcal_cycle_0 -niter 200000 coma_pbandB2_hanning.ms > selfcal_images/wsclean.log

gaincal(vis=f'coma_{name}_hanning.ms', caltable='selfcal/gains_cycle_0.cal', solint='inf', refant='ea27', gaintype='G', calmode='p')

# plotms(vis='selfcal/gains_cycle_0.cal', xaxis='time',yaxis='phase', iteraxis='antenna',coloraxis='corr', plotrange=[-1,-1,-180,180])

applycal(vis=f'coma_{name}_hanning.ms', gaintable='selfcal/gains_cycle_0.cal', calwt=False)

singularity exec singularity_image wsclean -size 5000 5000 -scale 2.5asec -data-column CORRECTED_DATA -update-model-required -reorder -weight briggs -0.5 -clean-border 1 -parallel-reordering 4 -gain 0.1 -mgain 0.7 -nmiter 30  -padding 1.4 -join-channels -channels-out 16 -local-rms -local-rms-strength 0.5 -auto-mask 3.0 -auto-threshold 0.5 -multiscale -multiscale-scale-bias 0.8 -multiscale-max-scales 7 -fit-spectral-pol 3 -pol i -gridder wgridder -fit-beam -dd-psf-grid 6 6 -parallel-deconvolution 2000 -name selfcal_images/selfcal_cycle_1 -niter 300000 coma_pbandB2_hanning.ms > selfcal_images/wsclean_sc1.log

gaincal(vis=f'coma_{name}_hanning.ms', caltable='selfcal/gains_cycle_1.cal', solint='300s', refant='ea27', gaintype='G', calmode='p')

# plotms(vis='selfcal/gains_cycle_1.cal', xaxis='time',yaxis='phase', iteraxis='antenna',coloraxis='corr', plotrange=[-1,-1,-180,180])

applycal(vis=f'coma_{name}_hanning.ms', gaintable='selfcal/gains_cycle_1.cal', calwt=False)

singularity exec singularity_image wsclean -size 5000 5000 -scale 2.5arcsec -data-column CORRECTED_DATA -update-model-required -reorder -weight briggs -0.5 -clean-border 1 -parallel-reordering 4 -gain 0.1 -mgain 0.7 -nmiter 30  -padding 1.4 -join-channels -channels-out 16 -local-rms -local-rms-strength 0.5 -auto-mask 3.0 -auto-threshold 0.5 -multiscale -multiscale-scale-bias 0.8 -multiscale-max-scales 7 -fit-spectral-pol 3 -pol i -gridder wgridder -fit-beam -dd-psf-grid 6 6 -parallel-deconvolution 2000 -name selfcal_images/selfcal_cycle_2 -niter 300000 coma_pbandB2_hanning.ms > selfcal_images/wsclean_sc2.log

gaincal(vis=f'coma_{name}_hanning.ms', caltable='selfcal/gains_cycle_2.cal', solint='200s', refant='ea27', gaintype='G', calmode='p')

# plotms(vis='selfcal/gains_cycle_2.cal', xaxis='time',yaxis='phase', iteraxis='antenna',coloraxis='corr', plotrange=[-1,-1,-180,180])

applycal(vis=f'coma_{name}_hanning.ms', gaintable='selfcal/gains_cycle_2.cal', calwt=False)

singularity exec singularity_image wsclean -size 5000 5000 -scale 2.5arcsec -data-column CORRECTED_DATA -update-model-required -reorder -weight briggs -0.5 -clean-border 1 -parallel-reordering 4 -gain 0.1 -mgain 0.7 -nmiter 30  -padding 1.4 -join-channels -channels-out 16 -local-rms -local-rms-strength 0.5 -auto-mask 3.0 -auto-threshold 0.5 -multiscale -multiscale-scale-bias 0.8 -multiscale-max-scales 7 -fit-spectral-pol 3 -pol i -gridder wgridder -fit-beam -dd-psf-grid 6 6 -parallel-deconvolution 2000 -name selfcal_images/selfcal_cycle_3 -niter 200000 coma_pbandB2_hanning.ms > selfcal_images/wsclean_sc3.log

gaincal(vis=f'coma_{name}_hanning.ms', caltable='selfcal/gains_cycle_3.cal', solint='100s', refant='ea27', gaintype='G', calmode='p')

# plotms(vis='selfcal/gains_cycle_3.cal', xaxis='time',yaxis='phase', iteraxis='antenna',coloraxis='corr', plotrange=[-1,-1,-180,180])

flagdata(vis=f'coma_{name}_hanning.ms', mode='manual', spw='0')

applycal(vis=f'coma_{name}_hanning.ms', gaintable='selfcal/gains_cycle_3.cal', calwt=False)

singularity exec singularity_image wsclean -size 5000 5000 -scale 2.5arcsec -data-column CORRECTED_DATA -update-model-required -reorder -weight briggs -0.5 -clean-border 1 -parallel-reordering 4 -gain 0.1 -mgain 0.7 -nmiter 30  -padding 1.4 -join-channels -channels-out 16 -local-rms -local-rms-strength 0.5 -auto-mask 3.0 -auto-threshold 0.5 -multiscale -multiscale-scale-bias 0.8 -multiscale-max-scales 7 -fit-spectral-pol 3 -pol i -gridder wgridder -fit-beam -dd-psf-grid 6 6 -parallel-deconvolution 2000 -name selfcal_images/selfcal_cycle_4 -niter 300000 coma_pbandB2_hanning.ms > selfcal_images/wsclean_sc4.log

gaincal(vis=f'coma_{name}_hanning.ms', caltable='selfcal/gains_cycle_4.cal', solint='80s', refant='ea27', gaintype='G', calmode='p')

# plotms(vis='selfcal/gains_cycle_4.cal', xaxis='time',yaxis='phase', iteraxis='antenna',coloraxis='corr', plotrange=[-1,-1,-180,180])

applycal(vis=f'coma_{name}_hanning.ms', gaintable='selfcal/gains_cycle_4.cal', calwt=False)

flagdata(vis=f'coma_{name}_hanning.ms', mode='rflag', datacolumn='corrected', action='apply', display='report', flagbackup=True, combinescans=True, ntime='3600s')

singularity exec singularity_image wsclean -size 5000 5000 -scale 2.5arcsec -data-column CORRECTED_DATA -update-model-required -reorder -weight briggs -0.5 -clean-border 1 -parallel-reordering 4 -gain 0.1 -mgain 0.7 -nmiter 30  -padding 1.4 -join-channels -channels-out 16 -local-rms -local-rms-strength 0.5 -auto-mask 3.0 -auto-threshold 0.5 -multiscale -multiscale-scale-bias 0.8 -multiscale-max-scales 7 -fit-spectral-pol 3 -pol i -gridder wgridder -fit-beam -dd-psf-grid 6 6 -parallel-deconvolution 2000 -name selfcal_images/selfcal_cycle_5 -niter 300000 coma_pbandB2_hanning.ms > selfcal_images/wsclean_sc5.log

gaincal(vis=f'coma_{name}_hanning.ms', caltable='selfcal/gains_cycle_5.cal', solint='60s', refant='ea27', gaintype='G', calmode='p')

# plotms(vis='selfcal/gains_cycle_5.cal', xaxis='time',yaxis='phase', iteraxis='antenna',coloraxis='corr', plotrange=[-1,-1,-180,180])

applycal(vis=f'coma_{name}_hanning.ms', gaintable='selfcal/gains_cycle_5.cal', calwt=False)

# flagdata(vis=f'coma_{name}_hanning.ms', mode='rflag', datacolumn='corrected', action='apply', display='report', flagbackup=True, combinescans=True, ntime='3600s')

singularity exec singularity_image wsclean -size 5100 5100 -scale 2.5arcsec -data-column CORRECTED_DATA -update-model-required -reorder -weight briggs -0.5 -clean-border 1 -parallel-reordering 4 -gain 0.1 -mgain 0.7 -nmiter 30  -padding 1.4 -join-channels -channels-out 16 -local-rms -local-rms-strength 0.5 -auto-mask 3.0 -auto-threshold 0.5 -multiscale -multiscale-scale-bias 0.8 -multiscale-max-scales 7 -fit-spectral-pol 3 -pol i -gridder wgridder -fit-beam -dd-psf-grid 6 6 -parallel-deconvolution 2000 -name selfcal_images/selfcal_cycle_6 -niter 300000 coma_pbandB2_hanning.ms > selfcal_images/wsclean_sc6.log

gaincal(vis=f'coma_{name}_hanning.ms', caltable='selfcal/gains_cycle_6.cal', solint='30s', refant='ea27', gaintype='G', calmode='p')

# plotms(vis='selfcal/gains_cycle_6.cal', xaxis='time',yaxis='phase', iteraxis='antenna',coloraxis='corr', plotrange=[-1,-1,-180,180])

applycal(vis=f'coma_{name}_hanning.ms', gaintable='selfcal/gains_cycle_6.cal', calwt=False)

flagdata(vis=f'coma_{name}_hanning.ms', mode='rflag', datacolumn='corrected', action='apply', display='report', flagbackup=True, combinescans=True, ntime='3600s')

singularity exec singularity_image wsclean -size 5100 5100 -scale 2.5arcsec -data-column CORRECTED_DATA -update-model-required -reorder -weight briggs 0.0 -clean-border 1 -parallel-reordering 4 -gain 0.1 -mgain 0.7 -nmiter 30  -padding 1.4 -join-channels -channels-out 16 -local-rms -local-rms-strength 0.5 -auto-mask 3.0 -auto-threshold 0.5 -multiscale -multiscale-scale-bias 0.8 -multiscale-max-scales 7 -fit-spectral-pol 3 -pol i -gridder wgridder -fit-beam -dd-psf-grid 6 6 -parallel-deconvolution 2000 -name selfcal_images/selfcal_cycle_7 -niter 300000 coma_pbandB2_hanning.ms > selfcal_images/wsclean_sc7.log

gaincal(vis=f'coma_{name}_hanning.ms', caltable='selfcal/gains_cycle_7.cal', solint='10s', refant='ea27', gaintype='G', calmode='p')

# plotms(vis='selfcal/gains_cycle_7.cal', xaxis='time',yaxis='phase', iteraxis='antenna',coloraxis='corr', plotrange=[-1,-1,-180,180])

# flag spw 14
flagdata(vis=f'coma_{name}_hanning.ms', mode='manual', spw='14')

applycal(vis=f'coma_{name}_hanning.ms', gaintable='selfcal/gains_cycle_7.cal', calwt=False)

flagdata(vis=f'coma_{name}_hanning.ms', mode='rflag', datacolumn='corrected-model', action='apply', display='report', flagbackup=True, combinescans=True, ntime='3600s')

singularity exec singularity_image wsclean -size 5100 5100 -scale 2.5arcsec -data-column CORRECTED_DATA -update-model-required -reorder -weight briggs 0.2 -clean-border 1 -parallel-reordering 4 -gain 0.1 -mgain 0.7 -nmiter 30  -padding 1.4 -join-channels -channels-out 16 -local-rms -local-rms-strength 0.5 -auto-mask 3.0 -auto-threshold 0.5 -multiscale -multiscale-scale-bias 0.8 -multiscale-max-scales 7 -fit-spectral-pol 3 -pol i -gridder wgridder -fit-beam -dd-psf-grid 6 6 -parallel-deconvolution 2000 -name selfcal_images/selfcal_cycle_8 -niter 300000 coma_pbandB2_hanning.ms > selfcal_images/wsclean_sc8.log

gaincal(vis=f'coma_{name}_hanning.ms', caltable='selfcal/gains_cycle_8.cal', solint='int', refant='ea27', gaintype='G', calmode='p')

# plotms(vis='selfcal/gains_cycle_8.cal', xaxis='time',yaxis='phase', iteraxis='antenna',coloraxis='corr', plotrange=[-1,-1,-180,180])

applycal(vis=f'coma_{name}_hanning.ms', gaintable='selfcal/gains_cycle_8.cal', calwt=False)

flagdata(vis=f'coma_{name}_hanning.ms', mode='rflag', datacolumn='corrected', action='apply', display='report', flagbackup=True, combinescans=True, ntime='3600s')

singularity exec singularity_image wsclean -size 5100 5100 -scale 2.5arcsec -data-column CORRECTED_DATA -update-model-required -reorder -weight briggs 0.2 -clean-border 1 -parallel-reordering 4 -gain 0.1 -mgain 0.7 -nmiter 30  -padding 1.4 -join-channels -channels-out 16 -local-rms -local-rms-strength 0.5 -auto-mask 3.0 -auto-threshold 0.5 -multiscale -multiscale-scale-bias 0.8 -multiscale-max-scales 7 -fit-spectral-pol 3 -pol i -gridder wgridder -fit-beam -dd-psf-grid 6 6 -parallel-deconvolution 2000 -name selfcal_images/selfcal_cycle_9 -niter 300000 coma_pbandB2_hanning.ms > selfcal_images/wsclean_sc9.log

gaincal(vis=f'coma_{name}_hanning.ms', caltable='selfcal/gains_cycle_9.cal', solint='inf', refant='ea27', gaintype='G', calmode='ap', solnorm=True, gaintable=['selfcal/gains_cycle_8.cal'])

# plotms(vis='selfcal/gains_cycle_9.cal', xaxis='time',yaxis='phase', iteraxis='antenna',coloraxis='corr', plotrange=[-1,-1,-180,180])

applycal(vis=f'coma_{name}_hanning.ms', gaintable='selfcal/gains_cycle_9.cal', calwt=False)

############ restored flagversion after gains_cycle_8 and then created image coma_pbandB0704_alpha ##############

flagdata(vis=f'coma_{name}_hanning.ms', mode='rflag', datacolumn='corrected', action='apply', display='report', flagbackup=True, combinescans=True, ntime='3600s')

singularity exec singularity_image wsclean -size 5100 5100 -scale 2.5arcsec -data-column CORRECTED_DATA -update-model-required -reorder -weight briggs 0.2 -clean-border 1 -parallel-reordering 4 -gain 0.1 -mgain 0.7 -nmiter 30  -padding 1.4 -join-channels -channels-out 16 -local-rms -local-rms-strength 0.5 -auto-mask 3.0 -auto-threshold 0.5 -multiscale -multiscale-scale-bias 0.8 -multiscale-max-scales 7 -fit-spectral-pol 3 -pol i -gridder wgridder -fit-beam -dd-psf-grid 6 6 -parallel-deconvolution 2000 -name selfcal_images/selfcal_cycle_10 -niter 300000 coma_pbandB2_hanning.ms > selfcal_images/wsclean_sc10.log

gaincal(vis=f'coma_{name}_hanning.ms', caltable='selfcal/gains_cycle_10.cal', solint='100s', refant='ea27', gaintype='G', calmode='ap', solnorm=True, gaintable=['selfcal/gains_cycle_8.cal'])

plotms(vis='selfcal/gains_cycle_10.cal', xaxis='time',yaxis='phase', iteraxis='antenna',coloraxis='corr', plotrange=[-1,-1,-180,180])

applycal(vis=f'coma_{name}_hanning.ms', gaintable='selfcal/gains_cycle_10.cal', calwt=False)

# flagdata(vis=f'coma_{name}_hanning.ms', mode='rflag', datacolumn='corrected', action='apply', display='report', flagbackup=True, combinescans=True, ntime='3600s')

singularity exec singularity_image wsclean -size 5100 5100 -scale 2.5arcsec -data-column CORRECTED_DATA -update-model-required -reorder -weight briggs 0.2 -clean-border 1 -parallel-reordering 4 -gain 0.1 -mgain 0.7 -nmiter 30  -padding 1.4 -join-channels -channels-out 16 -local-rms -local-rms-strength 0.5 -auto-mask 3.0 -auto-threshold 0.5 -multiscale -multiscale-scale-bias 0.8 -multiscale-max-scales 7 -fit-spectral-pol 3 -pol i -gridder wgridder -fit-beam -dd-psf-grid 6 6 -parallel-deconvolution 2000 -name selfcal_images/selfcal_cycle_11 -niter 300000 coma_pbandB2_hanning.ms > selfcal_images/wsclean_sc11.log

gaincal(vis=f'coma_{name}_hanning.ms', caltable='selfcal/gains_cycle_11.cal', solint='60s', refant='ea27', gaintype='G', calmode='ap'. solnorm=True, gaintable=['selfcal/gains_cycle_8.cal'])

plotms(vis='selfcal/gains_cycle_11.cal', xaxis='time',yaxis='phase', iteraxis='antenna',coloraxis='corr', plotrange=[-1,-1,-180,180])

applycal(vis=f'coma_{name}_hanning.ms', gaintable='selfcal/gains_cycle_11.cal', calwt=False)

flagdata(vis=f'coma_{name}_hanning.ms', mode='rflag', datacolumn='corrected', action='apply', display='report', flagbackup=True, combinescans=True, ntime='3600s')


######### for spectral index imaging #############
singularity exec singularity_image wsclean -size 5100 5100 -scale 2arcsec -data-column CORRECTED_DATA -no-update-model-required -beam-size 9arcsec -reorder -weight briggs 0.0 -clean-border 1 -parallel-reordering 4 -gain 0.1 -mgain 0.7 -nmiter 30  -padding 1.4 -join-channels -channels-out 16 -local-rms -local-rms-strength 0.5 -auto-mask 3.0 -auto-threshold 0.5 -multiscale -multiscale-scale-bias 0.8 -multiscale-max-scales 7 -fit-spectral-pol 3 -pol i -gridder wgridder -fit-beam -dd-psf-grid 6 6 -parallel-deconvolution 2000 -name coma_pbandB0704_alpha -niter 300000 coma_pbandB2_hanning.ms > coma_pband0705_alpha.log