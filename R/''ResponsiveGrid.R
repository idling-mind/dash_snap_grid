# AUTO GENERATED FILE - DO NOT EDIT

#' @export
''ResponsiveGrid <- function(children=NULL, id=NULL, allowOverlap=NULL, autoSize=NULL, breakpoints=NULL, cols=NULL, compactType=NULL, containerPadding=NULL, isBounded=NULL, isDraggable=NULL, isResizable=NULL, layout=NULL, layouts=NULL, margin=NULL, preventCollision=NULL, resizeHandles=NULL, rowHeight=NULL, transformScale=NULL, useCSSTransforms=NULL, width=NULL) {
    
    props <- list(children=children, id=id, allowOverlap=allowOverlap, autoSize=autoSize, breakpoints=breakpoints, cols=cols, compactType=compactType, containerPadding=containerPadding, isBounded=isBounded, isDraggable=isDraggable, isResizable=isResizable, layout=layout, layouts=layouts, margin=margin, preventCollision=preventCollision, resizeHandles=resizeHandles, rowHeight=rowHeight, transformScale=transformScale, useCSSTransforms=useCSSTransforms, width=width)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'ResponsiveGrid',
        namespace = 'dash_grid_layout',
        propNames = c('children', 'id', 'allowOverlap', 'autoSize', 'breakpoints', 'cols', 'compactType', 'containerPadding', 'isBounded', 'isDraggable', 'isResizable', 'layout', 'layouts', 'margin', 'preventCollision', 'resizeHandles', 'rowHeight', 'transformScale', 'useCSSTransforms', 'width'),
        package = 'dashGridLayout'
        )

    structure(component, class = c('dash_component', 'list'))
}
