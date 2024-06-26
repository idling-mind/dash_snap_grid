# AUTO GENERATED FILE - DO NOT EDIT

#' @export
''Grid <- function(children=NULL, id=NULL, cols=NULL, isDraggable=NULL, isResizable=NULL, layout=NULL, onLayoutChange=NULL, rowHeight=NULL) {
    
    props <- list(children=children, id=id, cols=cols, isDraggable=isDraggable, isResizable=isResizable, layout=layout, onLayoutChange=onLayoutChange, rowHeight=rowHeight)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'Grid',
        namespace = 'dash_grid_layout',
        propNames = c('children', 'id', 'cols', 'isDraggable', 'isResizable', 'layout', 'onLayoutChange', 'rowHeight'),
        package = 'dashGridLayout'
        )

    structure(component, class = c('dash_component', 'list'))
}
