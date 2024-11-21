import { Nav, NavLink, NavMenu } from "./NavbarElements";

const Navbar = () => {
    /* Navigation links - Home (defaault), and image Upload page */
    return (


        <Nav>
            <NavMenu>
                <NavLink to="/">Home</NavLink>
                <NavLink to="/image_upload">Image Upload</NavLink>
            </NavMenu>
        </Nav>
    );
};

export default Navbar;

