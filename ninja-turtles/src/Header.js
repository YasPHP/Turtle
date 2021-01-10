import React from "react";
import makestyles from "@material-ui/core"

const useStyles = makestyles{{
    header: {
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        marginTop: "20px"
    },
}};
export const Header = () => {
    const classes = useStyles({});
    return <div className={classes.header}></div>
};