from maya import cmds
def main():
    cmds.menu(l = 'Custom Tools', p ='MayaWindow', to = True)

    cmds.menuItem( subMenu=True, label='Setting' )
    cmds.menuItem( label='LeyerSetting', c = 'from mainEdit import layerSetting as ps; ps.main()')
    cmds.menuItem( optionBox=True, c = 'from mainEdit import layerSetting as ps; ps.option()')
    cmds.menuItem( label='autoRename', c = 'from mainEdit import autoRename as ps; ps.main()')
    cmds.menuItem( optionBox=True )
    cmds.setParent( '..', menu=True )

    cmds.menuItem( divider = True, dividerLabel = 'Modeling')
    cmds.menuItem( subMenu=True, label='CreateObjects', to = True)
    cmds.menuItem( label='Cube', i = 'polyCube.png', c = 'from createRenames import polyCubeCreateRename as ps; ps.main()')
    cmds.menuItem( label='Ball',  i = 'polySphere.png', c = 'from createRenames import polyBallCreateRename as ps; ps.main()')
    cmds.menuItem( label='Cylinder', i = 'polyCylinder.png', c = 'from createRenames import polyCylinderCreateRename as ps; ps.main()' )
    cmds.menuItem( label='Plean', i = 'polyMesh.png', c = 'from createRenames import polyPlaneCreateRename as ps; ps.main()' )
    cmds.menuItem( label='ImagePlean', i = 'ImagePlane.png', c = 'from createRenames import imagePlaneCreateRename as ps; ps.main()' )
    cmds.menuItem( label='Camera', i = 'view.png', c = 'from createRenames import cameraCreateRename as ps; ps.main()' )
    cmds.menuItem( label='AmbientLight', i = 'ambientlight.png', c = 'from createRenames import ambientLightCreateRename as ps; ps.main()' )
    cmds.menuItem( label='DirectionalLight', i = 'directionallight.png', c = 'from createRenames import directionalLightCreateRename as ps; ps.main()' )
    cmds.menuItem( label='PointLight', i = 'pointlight.png', c = 'from createRenames import pointLightCreateRename as ps; ps.main()' )
    cmds.menuItem( label='SpotLight',  i = 'spotlight.png', c = 'from createRenames import spotLightCreateRename as ps; ps.main()' )
    cmds.menuItem( label='Locator', i = 'locator.png', c = 'from createRenames import spaceLocatorCreateRename as ps; ps.main()' )
    cmds.menuItem( label='Joint', i = 'kinJoint.png', c = 'from createRenames import jointCreateRename as ps; ps.main()' )
    cmds.menuItem( label='ikHandle', i = 'kinHandle.png', c = 'from createRenames import ikHandleCreateRename as ps; ps.main()' )
    cmds.setParent( '..', menu=True )
    
    cmds.menuItem( subMenu=True, label='ModelingEdit', to = True)
    cmds.menuItem( label='CornerEdge', i = '//ennt/ENGI_Share/31_3DCG_Share/Maya_Scripts/tsuyuzakiScripts/icons/cornerEdge.png', c = 'from mainEdit import cornerEdgeSelect as ps; ps.main()')
    cmds.menuItem( label='Combine', i = 'polyUnite.png', c = 'from modelEdit import combineMesh as ps; ps.main()')
    cmds.menuItem( label='Extract' , i = 'polyChipOff.png', c = 'from modelEdit import extractComponent as ps; ps.main()')
    cmds.menuItem( label='HardEdge', i = 'polyHardEdge.png', c = 'from modelEdit import hardEdge as ps; ps.main()' )
    cmds.menuItem( label='SoftEdge', i = 'polySoftEdge.png', c = 'from modelEdit import softEdge as ps; ps.main()' )
    cmds.setParent( '..', menu=True )

    cmds.menuItem( divider = True, dividerLabel = 'Rigging')
    cmds.menuItem( subMenu=True, label='Skin', to = True)
    cmds.menuItem( label='skinPaintValue', c = 'from mainEdit import skinPaintValue as ps; ps.main()' )
    cmds.setParent( '..', menu=True )
    
    cmds.menuItem( subMenu=True, label='CreateCurves', to = True)
    cmds.menuItem( label='Antenna', c = 'from mayaPyCurves import curveAntenna as ps; ps.main()' )
    cmds.menuItem( label='Arrow1', c = 'from mayaPyCurves import curveArrow1 as ps; ps.main()' )
    cmds.menuItem( label='Arrow2', c = 'from mayaPyCurves import curveArrow2 as ps; ps.main()' )
    cmds.menuItem( label='Arrow4', c = 'from mayaPyCurves import curveArrow4 as ps; ps.main()' )
    cmds.menuItem( label='Circle', c = 'from mayaPyCurves import curveCircle as ps; ps.main()' )
    cmds.menuItem( label='Cube', c = 'from mayaPyCurves import curveCube as ps; ps.main()' )
    cmds.menuItem( label='Hexagon', c = 'from mayaPyCurves import curveHexagon as ps; ps.main()' )
    cmds.menuItem( label='Square', c = 'from mayaPyCurves import curveSquare as ps; ps.main()' )
    cmds.menuItem( label='Twist', c = 'from mayaPyCurves import curveTwist as ps; ps.main()' )
    cmds.menuItem( label='VectorIK', c = 'from mayaPyCurves import curveVectorIK as ps; ps.main()' )
    cmds.setParent( '..', menu=True )

    cmds.menuItem( subMenu=True, label='Constraint', to = True )
    cmds.menuItem( label='Parent', i = 'parentConstraint.png', c = 'from constraints import parentConstraintRename as ps; ps.main()')
    cmds.menuItem( label='Point', i = 'posConstraint.png', c = 'from constraints import pointConstraintRename as ps; ps.main()')
    cmds.menuItem( label='Orient', i = 'orientConstraint.png', c = 'from constraints import orientConstraintRename as ps; ps.main()')
    cmds.menuItem( label='Scale', i = 'scaleConstraint.png', c = 'from constraints import scaleConstraintRename as ps; ps.main()')
    cmds.menuItem( label='Aim', i = 'aimConstraint.png', c = 'from constraints import aimConstraintRename as ps; ps.main()')
    cmds.menuItem( label='PoleVector', i = 'poleVectorConstraint.png', c = 'from constraints import poleVectorConstraintRename as ps; ps.main()')
    cmds.menuItem( label='JointMatrix', c = 'from constraints import matrixJointConnect as ps; ps.main()')
    cmds.menuItem( label='ParentMatrix', c = 'from constraints import matrixParentConnect as ps; ps.main()')
    cmds.setParent( '..', menu=True )

    cmds.menuItem( subMenu=True, label='MirrorEdit', to = True )
    cmds.menuItem( label='CurveEditMirror', c = 'from mainEdit import curveMirror as ps; ps.main()')
    cmds.setParent( '..', menu=True )

    cmds.menuItem( subMenu=True, label='SelectsEdit', to = True )
    cmds.menuItem( label='CurveInSelects', c = 'from mainEdit import curveInSelect as ps; ps.main()')
    cmds.menuItem( label='OffsetCtrl', c = 'from mainEdit import ctrlOneConnect as ps; ps.main()')
    cmds.menuItem( optionBox=True )
    cmds.setParent( '..', menu=True )
    
    cmds.menuItem( divider = True, dividerLabel = 'Animator')
    cmds.menuItem( subMenu=True, label='CreateCtrl', to = True )
    cmds.menuItem( label='AddNullNode', c = 'from mainEdit import addNullNode as ps; ps.main()')
    cmds.setParent( '..', menu=True )

    cmds.menuItem( subMenu=True, label='Keyframe', to = True)
    cmds.menuItem( label='GrpCtrlAllKey', c = 'from mainEdit import grpCtrlAllKey as ps; ps.main()')
    cmds.menuItem( optionBox=True )
    cmds.setParent( '..', menu=True )