% Auto-generated: do not edit by hand
\name{''ResponsiveGrid}

\alias{''ResponsiveGrid}

\title{ResponsiveGrid component}

\description{

}

\usage{
''ResponsiveGrid(children=NULL, id=NULL, allowOverlap=NULL, autoSize=NULL,
breakpoints=NULL, cols=NULL, compactType=NULL,
containerPadding=NULL, draggableCancel=NULL,
draggableHandle=NULL, isBounded=NULL, isDraggable=NULL,
isResizable=NULL, layout=NULL, layouts=NULL, margin=NULL,
preventCollision=NULL, resizeHandles=NULL, rowHeight=NULL,
transformScale=NULL, useCSSTransforms=NULL, width=NULL)
}

\arguments{
\item{children}{The children of the grid}

\item{id}{The ID used to identify this component in Dash callbacks}

\item{allowOverlap}{allow overlapping in the grid}

\item{autoSize}{If true, container size swells to fit contents}

\item{breakpoints}{breakpoints for responsive design}

\item{cols}{The number of columns in the grid. This is an object with keys lg, md, sm, xs, xxs}

\item{compactType}{Compaction type}

\item{containerPadding}{Padding inside the container [x, y] in px. Can be an object with keys lg, md, sm, xs, xxs
and values [x, y]}

\item{draggableCancel}{A CSS selector for tags that will not be draggable
Use this to so that some elements like buttons register clicks as expected}

\item{draggableHandle}{A CSS selector for tags that will act as the draggable handle}

\item{isBounded}{Is bounded}

\item{isDraggable}{Whether the grid items are draggable}

\item{isResizable}{Whether the grid items are resizable}

\item{layout}{The layout of the grid, Readonly.}

\item{layouts}{The layouts of the grid}

\item{margin}{Margin between items [x, y] in px. Can be an object with keys lg, md, sm, xs, xxs
and values [x, y]}

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

