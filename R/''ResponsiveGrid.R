# AUTO GENERATED FILE - DO NOT EDIT

#' @export
''ResponsiveGrid <- function(children=NULL, id=NULL, allowOverlap=NULL, autoSize=NULL, breakpoints=NULL, cols=NULL, compactType=NULL, containerPadding=NULL, draggableCancel=NULL, draggableHandle=NULL, droppedItem=NULL, isBounded=NULL, isDraggable=NULL, isDroppable=NULL, isResizable=NULL, layout=NULL, layouts=NULL, margin=NULL, preventCollision=NULL, resizeHandles=NULL, rowHeight=NULL, transformScale=NULL, useCSSTransforms=NULL, width=NULL) {
    
    props <- list(children=children, id=id, allowOverlap=allowOverlap, autoSize=autoSize, breakpoints=breakpoints, cols=cols, compactType=compactType, containerPadding=containerPadding, draggableCancel=draggableCancel, draggableHandle=draggableHandle, droppedItem=droppedItem, isBounded=isBounded, isDraggable=isDraggable, isDroppable=isDroppable, isResizable=isResizable, layout=layout, layouts=layouts, margin=margin, preventCollision=preventCollision, resizeHandles=resizeHandles, rowHeight=rowHeight, transformScale=transformScale, useCSSTransforms=useCSSTransforms, width=width)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'ResponsiveGrid',
        namespace = 'dash_snap_grid',
        propNames = c('children', 'id', 'allowOverlap', 'autoSize', 'breakpoints', 'cols', 'compactType', 'containerPadding', 'draggableCancel', 'draggableHandle', 'droppedItem', 'isBounded', 'isDraggable', 'isDroppable', 'isResizable', 'layout', 'layouts', 'margin', 'preventCollision', 'resizeHandles', 'rowHeight', 'transformScale', 'useCSSTransforms', 'width'),
        package = 'dashSnapGrid'
        )

    structure(component, class = c('dash_component', 'list'))
}
