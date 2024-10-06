import React, { useEffect, useState } from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import MainMenu from './ui/components/nav';
import {MainLayout, ContentLayout} from "./ui/components/layout"
import { ThemeProvider } from '@mui/system';

import {hrtimeLight} from "./ui/material/theme.js"
import RegistrationsView from "./ui/pages/registrations/view.js"
import CardsView from "./ui/pages/cards/view.js"
import DepartmentsView from "./ui/pages/departments/view.js"
import UsersView from "./ui/pages/users/view.js"

// TODO probably theme is not prefiled
//
//
function App() {
    const [loading, setLoading] = useState(false);
    const [progress, setProgress] = useState(0);
    useEffect(() => {
	console.log("TODO: Loading...")
    }, []);

    return (
	<div id='app' className="app">
	    <ThemeProvider theme={hrtimeLight}>
		<MainLayout>
		    <Router basename={process.env.PUBLIC_URL}>
			<MainMenu />
			<ContentLayout>
			    <Routes>
				<Route path="/" element={<RegistrationsView/>} />
				<Route path="/cards" element={<CardsView />} />
				<Route path="/users" element={<UsersView />} />
				<Route path="/departments" element={<DepartmentsView />} />
			    </Routes>
			</ContentLayout>
		    </Router>
		</MainLayout>
	    </ThemeProvider>
	</div>
    );
};

export default App;
