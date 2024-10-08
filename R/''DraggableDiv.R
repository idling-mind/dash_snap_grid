# AUTO GENERATED FILE - DO NOT EDIT

#' @export
''DraggableDiv <- function(children=NULL, id=NULL, style=NULL) {
    
    props <- list(children=children, id=id, style=style)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'DraggableDiv',
        namespace = 'dash_snap_grid',
        propNames = c('children', 'id', 'style'),
        package = 'dashSnapGrid'
        )

    structure(component, class = c('dash_component', 'list'))
}
