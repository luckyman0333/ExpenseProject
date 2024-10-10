import React, { useState, useRef, useLayoutEffect, useCallback } from 'react'
import Table from '@mui/material/Table'
import TableBody from '@mui/material/TableBody'
import TableCell from '@mui/material/TableCell'
import TableContainer from '@mui/material/TableContainer'
import TableHead from '@mui/material/TableHead'
import TableRow from '@mui/material/TableRow'
import CircularProgress from '@mui/material/CircularProgress'
import { styled } from '@mui/material/styles'
// const generateItems = amount => {
//     const arr = Array.from(Array(amount))
//     return arr.map((number, i) => ({
//         id: i,
//         name: `Name ${i + 1}`,
//         type: `Item Type ${i + 1}`,
//     }))
// }

{/* to do, move it to themes!! */}
const StyledTableCell = styled(TableCell)({
    "& .MuiTableCell-head": {  // or "& .MuiTableCell-root" or "& .MuiTableCell-body" ...
        //backgroundColor: "#99D9EA",
        fontWeight: 600
    }
});

const TableWithInfiniteScroll = ({ columns, rows }) => {
    const tableEl = useRef()
    //const [rows, setRows] = useState(generateItems(50))
    const [loading, setLoading] = useState(false)
    const [distanceBottom, setDistanceBottom] = useState(0)
    // hasMore should come from the place where you do the data fetching
    // for example, it could be a prop passed from the parent component
    // or come from some store
    const [hasMore] = useState(true)
    const loadMore = useCallback(() => {
        const loadItems = async () => {
            await new Promise(resolve =>
                setTimeout(() => {
                    const amount = rows.length + 50
                   // setRows(generateItems(amount))
                    setLoading(false)
                    resolve()
                }, 2000),
            )
        }
        setLoading(true)
        loadItems()
    }, [rows])
    const scrollListener = useCallback(() => {
        let bottom = tableEl.current.scrollHeight - tableEl.current.clientHeight
        // if you want to change distanceBottom every time new data is loaded
        // don't use the if statement
        if (!distanceBottom) {
            // calculate distanceBottom that works for you
            setDistanceBottom(Math.round(bottom * 0.2))
        }
        if (tableEl.current.scrollTop > bottom - distanceBottom && hasMore && !loading) {
            loadMore()
        }
    }, [hasMore, loadMore, loading, distanceBottom])
    useLayoutEffect(() => {
        const tableRef = tableEl.current
        tableRef.addEventListener('scroll', scrollListener)
        return () => {
            tableRef.removeEventListener('scroll', scrollListener)
        }
    }, [scrollListener])
    return (
        <TableContainer sx={{maxHeight: '80vh', minHeight: '80vh'}} ref={tableEl}>
            {/* to do, check this circular, top!! */}
            {loading && <CircularProgress style={{ position: 'absolute', top: '100px' }} />}
            <Table>
                <StyledTableCell>
                <TableHead>
                    <TableRow>
                        {columns.map((column) => (
                            <TableCell>{column.title}</TableCell>
                        ))}
                    </TableRow>
                </TableHead>

                <TableBody>
                    {rows.map(( row ) => (
                        <TableRow key={row.card_nr}> {/* to do!!, rewrite it to not static!! */}
                            <TableCell>{row.first_name}</TableCell>
                            <TableCell>{row.last_name}</TableCell>
                            <TableCell>{row.act}</TableCell>
                            <TableCell>{row.card_nr}</TableCell>
                            <TableCell>{row.work_type}</TableCell>
                            <TableCell>{row.datetime}</TableCell>
                            <TableCell>{row.section}</TableCell>
                            <TableCell>{row.direction}</TableCell>
                        </TableRow>))}
                </TableBody>
                </StyledTableCell>
            </Table>
        </TableContainer>)
}
export {TableWithInfiniteScroll};
