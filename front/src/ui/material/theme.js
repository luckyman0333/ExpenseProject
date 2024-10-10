// import { createTheme } from '@mui/system';
import { createTheme } from '@mui/material/styles';
import { green, purple } from '@mui/material/colors';

const hrtimeLight = createTheme({
    typography:{
	button: {
	    textTransform: 'none'
	}
    },
    palette: {
	primary: {
	    main: '#1976d2',
	    contrastText: 'white'
	}
    }
});


export {hrtimeLight};
