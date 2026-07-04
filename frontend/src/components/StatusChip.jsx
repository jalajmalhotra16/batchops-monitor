import Chip from "@mui/material/Chip";

function StatusChip({ status }) {

    let color = "default";

    if (status === "Succeeded") {
        color = "success";
    }
    else if (status === "Failed") {
        color = "error";
    }
    else if (status === "Running") {
        color = "warning";
    }

    return (
        <Chip
            label={status || "Unknown"}
            color={color}
            size="small"
        />
    );
}

export default StatusChip;