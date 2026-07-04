import {

    Paper,
    Table,
    TableBody,
    TableCell,
    TableContainer,
    TableHead,
    TableRow

} from "@mui/material";

import StatusChip from "./StatusChip";

function DashboardTable({ cronJobs }) {

    return (

        <TableContainer component={Paper} elevation={3}>

            <Table>

                <TableHead>

                    <TableRow>

                        <TableCell><b>CronJob</b></TableCell>

                        <TableCell><b>Status</b></TableCell>

                        <TableCell><b>Schedule</b></TableCell>

                        <TableCell><b>Last Run</b></TableCell>

                    </TableRow>

                </TableHead>

                <TableBody>

                    {cronJobs.map((job) => (

                        <TableRow
                            key={job.cronJob}
                            hover
                        >

                            <TableCell>

                                {job.cronJob}

                            </TableCell>

                            <TableCell>

                                <StatusChip
                                    status={job.lastExecution?.status}
                                />

                            </TableCell>

                            <TableCell>

                                {job.schedule}

                            </TableCell>

                            <TableCell>

                                {

                                    job.lastScheduleTime
                                        ? new Date(job.lastScheduleTime).toLocaleString()
                                        : "-"

                                }

                            </TableCell>

                        </TableRow>

                    ))}

                </TableBody>

            </Table>

        </TableContainer>

    );

}

export default DashboardTable;