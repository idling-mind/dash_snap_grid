
module DashSnapGrid
using Dash

const resources_path = realpath(joinpath( @__DIR__, "..", "deps"))
const version = "0.0.1"

include("jl/''_draggablediv.jl")
include("jl/''_grid.jl")
include("jl/''_responsivegrid.jl")

function __init__()
    DashBase.register_package(
        DashBase.ResourcePkg(
            "dash_snap_grid",
            resources_path,
            version = version,
            [
                DashBase.Resource(
    relative_package_path = "dash_snap_grid.min.js",
    external_url = nothing,
    dynamic = nothing,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "dash_snap_grid.min.js.map",
    external_url = nothing,
    dynamic = true,
    async = nothing,
    type = :js
)
            ]
        )

    )
end
end
