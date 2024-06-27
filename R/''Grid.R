# AUTO GENERATED FILE - DO NOT EDIT

#' @export
''Grid <- function(children=NULL, id=NULL, allowOverlap=NULL, autoSize=NULL, cols=NULL, compactType=NULL, containerPadding=NULL, isDraggable=NULL, isResizable=NULL, layout=NULL, margin=NULL, preventCollision=NULL, resizeHandles=NULL, rowHeight=NULL, width=NULL) {
    
    props <- list(children=children, id=id, allowOverlap=allowOverlap, autoSize=autoSize, cols=cols, compactType=compactType, containerPadding=containerPadding, isDraggable=isDraggable, isResizable=isResizable, layout=layout, margin=margin, preventCollision=preventCollision, resizeHandles=resizeHandles, rowHeight=rowHeight, width=width)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'Grid',
        namespace = 'dash_grid_layout',
        propNames = c('children', 'id', 'allowOverlap', 'autoSize', 'cols', 'compactType', 'containerPadding', 'isDraggable', 'isResizable', 'layout', 'margin', 'preventCollision', 'resizeHandles', 'rowHeight', 'width'),
        package = 'dashGridLayout'
        )

    structure(component, class = c('dash_component', 'list'))
}
