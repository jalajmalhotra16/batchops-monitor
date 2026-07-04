import { useEffect, useState } from "react";
import api from "../api/api";

import DashboardTable from "../components/DashboardTable";

import {
    AppBar,
    Toolbar,
    Typography,
    Container,
    Box,
    Button,
    TextField
} from "@mui/material";

import RefreshIcon from "@mui/icons-material/Refresh";

function Dashboard() {

    const [cronJobs, setCronJobs] = useState([]);
    const [search, setSearch] = useState("");

    async function fetchDashboard() {

        try {

            const response = await api.get("/dashboard");
            setCronJobs(response.data);

        } catch (error) {

            console.error(error);

        }

    }

    useEffect(() => {

        fetchDashboard();

    }, []);

    const filteredCronJobs = cronJobs.filter((job) =>
        job.cronJob.toLowerCase().includes(search.toLowerCase())
    );

    return (

        <>

            <AppBar position="static">

                <Toolbar>

                    <Typography
                        variant="h6"
                        sx={{ flexGrow: 1 }}
                    >

                        BatchOps

                    </Typography>

                    <Button
                        color="inherit"
                        startIcon={<RefreshIcon />}
                        onClick={fetchDashboard}
                    >

                        Refresh

                    </Button>

                </Toolbar>

            </AppBar>

            <Container
                maxWidth="lg"
                sx={{ mt: 4 }}
            >

                <Typography variant="h4">

                    Kubernetes Batch Operations Platform

                </Typography>

                <Typography
                    color="text.secondary"
                    sx={{ mb: 4 }}
                >

                    Monitor Kubernetes CronJobs, Jobs and Pods

                </Typography>

                <Box
                    display="flex"
                    justifyContent="space-between"
                    mb={3}
                >

                    <TextField
                        label="Search CronJobs"
                        value={search}
                        onChange={(e) => setSearch(e.target.value)}
                        size="small"
                        sx={{ width: 300 }}
                    />

                    <Typography variant="h6">

                        Total CronJobs : {filteredCronJobs.length}

                    </Typography>

                </Box>

                <DashboardTable cronJobs={filteredCronJobs} />

            </Container>

        </>

    );

}

export default Dashboard;