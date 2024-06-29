% Auto-generated: do not edit by hand
\name{''Grid}

\alias{''Grid}

\title{Grid component}

\description{

}

\usage{
''Grid(children=NULL, id=NULL, allowOverlap=NULL, autoSize=NULL,
cols=NULL, compactType=NULL, containerPadding=NULL,
draggableCancel=NULL, draggableHandle=NULL,
droppedItem=NULL, isBounded=NULL, isDraggable=NULL,
isDroppable=NULL, isResizable=NULL, layout=NULL,
margin=NULL, preventCollision=NULL, resizeHandles=NULL,
rowHeight=NULL, transformScale=NULL, useCSSTransforms=NULL,
width=NULL)
}

\arguments{
\item{children}{The children of the grid}

\item{id}{The ID used to identify this component in Dash callbacks}

\item{allowOverlap}{allow overlapping in the grid}

\item{autoSize}{If true, container size swells to fit contents}

\item{cols}{The number of columns in the grid}

\item{compactType}{Compaction type}

\item{containerPadding}{Padding inside the container [x, y] in px}

\item{draggableCancel}{A CSS selector for tags that will not be draggable
Use this to so that some elements like buttons register clicks as expected}

\item{draggableHandle}{A CSS selector for tags that will act as the draggable handle}

\item{droppedItem}{ID of the dropped element}

\item{isBounded}{Is bounded}

\item{isDraggable}{Whether the grid items are draggable}

\item{isDroppable}{if true, droppable elements (with draggable=true) can be dropped on the grid
droppedItem is the id of the dropped element}

\item{isResizable}{Whether the grid items are resizable}

\item{layout}{The layout of the grid}

\item{margin}{Margin between items [x, y] in px}

\item{preventCollision}{If true, grid items wont change position when being dragged over}

\item{resizeHandles}{Which resize handles to display
s, e, w, n, se, ne, sw, nw}

\item{rowHeight}{The row height of the grid. Default is 150.}

\item{transformScale}{If parent DOM node of ResponsiveReactGridLayout or ReactGridLayout has "transform: scale(n)" css property,
we should set scale coefficient to avoid render artefacts while dragging.}

\item{useCSSTransforms}{Uses CSS3 `translate()` instead of position top/left.
This makes about 6x faster paint performance}

\item{width}{Initial width of the grid}
}

\value{named list of JSON elements corresponding to React.js properties and their values}

