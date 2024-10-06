import React, { useEffect, useState } from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import MainMenu from './ui/components/nav';
import {MainLayout, ContentLayout} from "./ui/components/layout"
import { ThemeProvider } from '@mui/system';

import {hrtimeLight} from "./ui/material/theme.js"
import RegistrationsView from "./ui/registrations/view.js"
import CardsView from "./ui/cards/view.js"
import DepartmentsView from "./ui/departments/view.js"
import UsersView from "./ui/users/view.js"

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
