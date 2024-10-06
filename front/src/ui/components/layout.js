import React from "react";
import { Link, useLocation } from 'react-router-dom';
import logo from '../../images/hrtime.png';
import Box from '@mui/material/Box';
import { styled, createTheme, ThemeProvider } from '@mui/system';

const MainLayout = styled(Box)(({ theme }) => ({
    height:      "100vh",
    overflow:    "hidden",
    background:  "default",
    display:     "flex"
}));

const ContentLayout = styled(Box)(({ theme }) => ({
    overflow:   "hidden",
    height:     "100%",
    width:      "100%"
}));


export {MainLayout, ContentLayout};
