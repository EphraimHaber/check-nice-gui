from nicegui import ui
import pandas as pd
from frontend.core import header
from typing import Optional, TypedDict, Any, Literal
import itertools

MyRenderer = """
class MissionResultRenderer {
	eGui;

	init(params) {
        // console.log(params);
		const icon = document.createElement('img');
		icon.src = `https://www.ag-grid.com/example-assets/icons/tick-in-circle.png`;
		icon.setAttribute('class', 'missionIcon');

		this.eGui = document.createElement('div');
        if (params.value) {
		    this.eGui.setAttribute('class', 'flex items-center h-full w-full');
		    this.eGui.appendChild(icon);
        }
	}

	getGui() {
		return this.eGui;
	}

	refresh(params) {
		return false;
	}
}

"""

CustomTooltip = """
class CustomTooltip {
    init(params) {
        console.log(params);
        this.eGui = document.createElement('div');
        this.eGui.style.cssText = 'background: black; color: white; padding: 5px; border-radius: 5px';
        this.eGui.innerText = params.value;
    }
    getGui() {
        return this.eGui;
    }
}
"""


class GridOptions(TypedDict):
    statusBar: Optional[Any]
    sideBar: Optional[Any]
    suppressContextMenu: Optional[bool]
    preventDefaultOnContextMenu: Optional[bool]
    allowContextMenuWithControlKey: Optional[bool]
    columnMenu: Optional[Literal["legacy", "new"]]
    suppressMenuHide: Optional[bool]
    enableBrowserTooltips: Optional[bool]
    tooltipTrigger: Optional[Literal["hover", "focus"]]
    tooltipShowDelay: Optional[int]
    tooltipHideDelay: Optional[int]
    tooltipMouseTrack: Optional[bool]
    tooltipShowMode: Optional[Literal["standard", "whenTruncated"]]
    tooltipInteraction: Optional[bool]
    popupParent: Optional[Any]
    copyHeadersToClipboard: Optional[bool]
    copyGroupHeadersToClipboard: Optional[bool]
    clipboardDelimiter: Optional[str]
    suppressCopyRowsToClipboard: Optional[bool]
    suppressCopySingleCellRanges: Optional[bool]
    suppressLastEmptyLineOnPaste: Optional[bool]
    suppressClipboardPaste: Optional[bool]
    suppressClipboardApi: Optional[bool]
    suppressCutToClipboard: Optional[bool]
    # TODO continue


class ColDef(TypedDict):
    headerName: str
    field: str
    hide: bool
    cellClassRules: dict[str, str]


# Define the input values
who_values = ["me", "not_me"]
where_values = ["here", "not_here"]
keyid_values = ["KeyId.id", "KeyId.arn", "KeyId.alias"]
output_values = [
    {"outcome": "passed", "crashed": True},
    {"outcome": "passed", "crashed": False},
    {"outcome": "failed", "crashed": True},
    {"outcome": "failed", "crashed": False},
]
policy_values = ["all", "none"]

all_permutations = list(itertools.product(who_values, where_values, keyid_values, output_values, policy_values))
formatted_permutations = []
for perm in all_permutations:
    formatted_perm = {"who": perm[0], "where": perm[1], "KeyId": perm[2], perm[4]: perm[3]}
    formatted_permutations.append(formatted_perm)


@ui.page("/table")
async def table_viewer():
    header()
    data_df = pd.DataFrame(formatted_permutations)
    ag_grid_options = {
        "columnDefs": [
            {"headerName": "Who", "field": "who"},
            {"headerName": "Where", "field": "where"},
            {"headerName": "KeyId", "field": "KeyId", "tooltipField": "KeyId", ":tooltipComponent": CustomTooltip},
            {
                "headerName": "all",
                "field": "all",
                ":cellRenderer": MyRenderer,
                "tooltipField": "all",
                ":tooltipComponent": CustomTooltip,
            },
            {"headerName": "none", "field": "none", ":cellRenderer": MyRenderer, "tooltipComponent": CustomTooltip},
        ],
        "rowData": data_df.to_dict("records"),
        "tooltipShowDelay": 100,
    }
    ui.aggrid(ag_grid_options).on("cellClicked", lambda event: ui.notify(f"Cell value: {event.args['value']}")).classes(
        "h-[80vh]"
    )
