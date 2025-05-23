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
draggableHandle=NULL, droppedItem=NULL, isBounded=NULL,
isDraggable=NULL, isDroppable=NULL, isResizable=NULL,
layout=NULL, layouts=NULL, margin=NULL,
preventCollision=NULL, resizeHandles=NULL, rowHeight=NULL,
transformScale=NULL, useCSSTransforms=NULL, width=NULL)
}

\arguments{
\item{children}{A list of or a singular dash component, string or number. The children of the grid}

\item{id}{Character. The ID used to identify this component in Dash callbacks}

\item{allowOverlap}{Logical. allow overlapping in the grid}

\item{autoSize}{Logical. If true, container size swells to fit contents}

\item{breakpoints}{Named list. breakpoints for responsive design}

\item{cols}{Named list. The number of columns in the grid. This is an object with keys lg, md, sm, xs, xxs}

\item{compactType}{A value equal to: 'vertical', 'horizontal', null. Compaction type}

\item{containerPadding}{Padding inside the container [x, y] in px. Can be an object with keys lg, md, sm, xs, xxs
and values [x, y]}

\item{draggableCancel}{Character. A CSS selector for tags that will not be draggable
Use this to so that some elements like buttons register clicks as expected}

\item{draggableHandle}{Character. A CSS selector for tags that will act as the draggable handle}

\item{droppedItem}{Named list. ID of the dropped element}

\item{isBounded}{Logical. Is bounded}

\item{isDraggable}{Logical. Whether the grid items are draggable}

\item{isDroppable}{Logical. if true, droppable elements (with draggable=true) can be dropped on the grid
droppedItem is the layout information of the dropped element}

\item{isResizable}{Logical. Whether the grid items are resizable}

\item{layout}{List of named lists. The layout of the grid, Readonly.}

\item{layouts}{Named list. The layouts of the grid}

\item{margin}{Margin between items [x, y] in px. Can be an object with keys lg, md, sm, xs, xxs
and values [x, y]}

\item{preventCollision}{Logical. If true, grid items wont change position when being dragged over}

\item{resizeHandles}{List of characters. Which resize handles to display
s, e, w, n, se, ne, sw, nw}

\item{rowHeight}{Numeric. The row height of the grid. Default is 150.}

\item{transformScale}{Numeric. If parent DOM node of ResponsiveReactGridLayout or ReactGridLayout has "transform: scale(n)" css property,
we should set scale coefficient to avoid render artefacts while dragging.}

\item{useCSSTransforms}{Logical. Uses CSS3 `translate()` instead of position top/left.
This makes about 6x faster paint performance}

\item{width}{Numeric. Initial width of the grid}
}

\value{named list of JSON elements corresponding to React.js properties and their values}

