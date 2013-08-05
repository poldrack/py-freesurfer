"""
python class to represent a freesurfer directory

"""

import os

class Freesurfer:
    """
    this is the main class that represents a freesurfer subject directory
    """

    files={}
    
    def __init__(self,dir,verbose=False):

        self.verbose=verbose
        if not os.path.exists(dir):
            raise IOError('%s does not exist'%dir)
        self.dir=dir

       self.data=getFreesurferDirStructure()
        
        for d in fs_subdirs.iterkeys():
            if os.path.exists(d):
                self.files[d]={}
            else:
                self.files[d]=None
            
    
    def getFreesurferDirStructure():
        """
        return a structure that describes a full freesurfer directory
        """
        files={}
        files['label']=['aparc.annot.a2009s.ctab', 'aparc.annot.ctab','BA.ctab','lh.aparc.a2009s.annot','lh.aparc.annot','lh.BA.annot','lh.BA1.label','lh.BA2.label','lh.BA3a.label','lh.BA3b.label','lh.BA44.label','lh.BA45.label','lh.BA4a.label','lh.BA4p.label','lh.BA6.label','lh.cortex.label','lh.entorhinal_exvivo.label','lh.MT.label', 'lh.V1.label', 'lh.V2.label', 'rh.aparc.a2009s.annot', 'rh.aparc.annot', 'rh.BA.annot', 'rh.BA1.label', 'rh.BA2.label', 'rh.BA3a.label', 'rh.BA3b.label', 'rh.BA44.label', 'rh.BA45.label', 'rh.BA4a.label', 'rh.BA4p.label', 'rh.BA6.label', 'rh.cortex.label', 'rh.entorhinal_exvivo.label', 'rh.MT.label', 'rh.V1.label','rh.V2.label']
        files['mri']=['aparc+aseg.mgz', 'aparc.a2009s+aseg.mgz', 'aseg.auto.mgz', 'aseg.auto_noCCseg.label_intensities.txt', 'aseg.auto_noCCseg.mgz', 'aseg.mgz', 'aseg_labels.txt', 'brain.finalsurfs.mgz', 'brain.mgz', 'brainmask.auto.mgz', 'brainmask.mgz', 'brainmask.nii.gz', 'ctrl_pts.mgz', 'filled.mgz', 'lh.ribbon.mgz', 'mni152.orig.mgz', 'mni152.orig.mgz.reg', 'mri_nu_correct.mni.log', 'norm.mgz', 'nu.mgz', 'nu_noneck.mgz', 'orig', 'orig.mgz', 'rawavg.mgz', 'rh.ribbon.mgz', 'ribbon.mgz', 'segment.dat', 'T1.mgz', 'talairach.label_intensities.txt', 'transforms', 'ventrices.mgz', 'ventrices.nii.gz', 'wm.asegedit.mgz', 'wm.mgz', 'wm.seg.mgz', 'wmparc.mgz']
        files['scripts']=['build-stamp.txt','csurfdir', 'mni152reg.log', 'ponscc.cut.log', 'recon-all-status.log', 'recon-all.cmd', 'recon-all.done', 'recon-all.env', 'recon-all.env.bak', 'recon-all.local-copy', 'recon-all.log']
        files['stats']=['aseg.stats','lh.aparc.a2009s.stats', 'lh.aparc.stats', 'lh.BA.stats', 'lh.entorhinal_exvivo.stats', 'rh.aparc.a2009s.stats', 'rh.aparc.stats', 'rh.BA.stats', 'rh.entorhinal_exvivo.stats', 'wmparc.stats']
        files['surf']=['lh.area', 'lh.area.mid', 'lh.area.pial', 'lh.avg_curv', 'lh.curv', 'lh.curv.pial', 'lh.defect_borders', 'lh.defect_chull', 'lh.defect_labels', 'lh.inflated', 'lh.inflated.H', 'lh.inflated.K', 'lh.inflated.nofix', 'lh.jacobian_white', 'lh.orig', 'lh.orig.nofix', 'lh.pial', 'lh.qsphere.nofix', 'lh.smoothwm', 'lh.smoothwm.nofix', 'lh.sphere', 'lh.sphere.reg', 'lh.sulc', 'lh.thickness', 'lh.volume', 'lh.white', 'rh.area', 'rh.area.mid', 'rh.area.pial', 'rh.avg_curv', 'rh.curv', 'rh.curv.pial', 'rh.defect_borders', 'rh.defect_chull', 'rh.defect_labels', 'rh.inflated', 'rh.inflated.H', 'rh.inflated.K', 'rh.inflated.nofix', 'rh.jacobian_white', 'rh.orig', 'rh.orig.nofix', 'rh.pial', 'rh.qsphere.nofix', 'rh.smoothwm', 'rh.smoothwm.nofix', 'rh.sphere', 'rh.sphere.reg', 'rh.sulc', 'rh.thickness', 'rh.volume', 'rh.white']

        return files
        
