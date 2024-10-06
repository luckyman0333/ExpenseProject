import React from "react";
import { Link, useLocation } from 'react-router-dom';
import routes from '../../data/routes.json';
import logo from '../../images/hrtime.png';
import Stack from '@mui/material/Stack';
import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';
import { styled } from '@mui/system';




const StyledMainMeny = styled(Stack)(({ theme }) => ({
    // color: theme.palette.primary.contrastText,
    // backgroundColor: theme.palette.primary.main,
    backgroundColor: "white",
    padding: theme.spacing(1),
    width:  "220px",
    minWidth: "200px",
    color: "black",
    //borderRight: "1px solid #ebebeb",
    boxShadow: "0px 0px 5px #ebebeb"
}));


function MenuItem(props) {
  const location = useLocation();
  const isActive = () => {
    const currentPath = location.pathname;
    const linkPath = props.to;
    if (currentPath === linkPath) {return true;}
    if (currentPath.startsWith(linkPath + '/') && linkPath !== '/') {return true;}
    return false;};
  return (
      <Button variant={`${isActive() ? 'contained': 'text'}`} href={props.to}>{props.children}</Button>
  );
}



function MainMenu() {
  return (
      <StyledMainMeny>
	  <Stack justifyContent="space-between" alignItems="center" sx={{height: "100%"}}>
	      <Stack spacing={2}>
		  <Stack direction="column" spacing={1}>
		      <Stack direction="column" justifyItems="center" alignItems="center">
			  <img src={logo} width="50%" alt="logo" />
		      </Stack>
		  </Stack>
		  <Stack>
		      {routes.mainRoutes.map((route) =>
			  <MenuItem key={route.path} to={route.path}>{route.label}</MenuItem>
		      )}
		  </Stack>
	      </Stack>
	      {process.env.NODE_ENV === 'development' ?
	       <Stack><Typography sx={{color: "#ff9696"}}>dev mode</Typography></Stack> :
	       null}
	  
	  </Stack>
    </StyledMainMeny>
  );
}

export default MainMenu;
