# AUTO GENERATED FILE - DO NOT EDIT

#' @export
''Grid <- function(children=NULL, id=NULL, allowOverlap=NULL, autoSize=NULL, cols=NULL, compactType=NULL, containerPadding=NULL, draggableCancel=NULL, draggableHandle=NULL, droppedItem=NULL, isBounded=NULL, isDraggable=NULL, isDroppable=NULL, isResizable=NULL, layout=NULL, margin=NULL, preventCollision=NULL, resizeHandles=NULL, rowHeight=NULL, transformScale=NULL, useCSSTransforms=NULL, width=NULL) {
    
    props <- list(children=children, id=id, allowOverlap=allowOverlap, autoSize=autoSize, cols=cols, compactType=compactType, containerPadding=containerPadding, draggableCancel=draggableCancel, draggableHandle=draggableHandle, droppedItem=droppedItem, isBounded=isBounded, isDraggable=isDraggable, isDroppable=isDroppable, isResizable=isResizable, layout=layout, margin=margin, preventCollision=preventCollision, resizeHandles=resizeHandles, rowHeight=rowHeight, transformScale=transformScale, useCSSTransforms=useCSSTransforms, width=width)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'Grid',
        namespace = 'dash_grid_layout',
        propNames = c('children', 'id', 'allowOverlap', 'autoSize', 'cols', 'compactType', 'containerPadding', 'draggableCancel', 'draggableHandle', 'droppedItem', 'isBounded', 'isDraggable', 'isDroppable', 'isResizable', 'layout', 'margin', 'preventCollision', 'resizeHandles', 'rowHeight', 'transformScale', 'useCSSTransforms', 'width'),
        package = 'dashGridLayout'
        )

    structure(component, class = c('dash_component', 'list'))
}
