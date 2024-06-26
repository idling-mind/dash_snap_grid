# AUTO GENERATED FILE - DO NOT EDIT

#' @export
''GridItem <- function(children=NULL, id=NULL, bounded=NULL, draggable=NULL, height=NULL, max_height=NULL, max_width=NULL, min_height=NULL, min_width=NULL, resizable=NULL, static=NULL, style=NULL, width=NULL, x=NULL, y=NULL) {
    
    props <- list(children=children, id=id, bounded=bounded, draggable=draggable, height=height, max_height=max_height, max_width=max_width, min_height=min_height, min_width=min_width, resizable=resizable, static=static, style=style, width=width, x=x, y=y)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'GridItem',
        namespace = 'dash_grid_layout',
        propNames = c('children', 'id', 'bounded', 'draggable', 'height', 'max_height', 'max_width', 'min_height', 'min_width', 'resizable', 'static', 'style', 'width', 'x', 'y'),
        package = 'dashGridLayout'
        )

    structure(component, class = c('dash_component', 'list'))
}
