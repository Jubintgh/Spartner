import React from 'react';
import "./Footer.css";

const Footer = () => {
    return (
        <div className="main-footer">
            <div className="footer-container">
                <div className="footer-content-row-1">
                    {/* column1 */}
                    <div className="footer-col-row1">
                        <img/>
                        <h3>Name here</h3>
                    </div>
                    {/* column2 */}
                    <div className="footer-col-row1">
                        <img/>
                        <h3>Name here</h3>
                    </div>
                    {/* column3 */}
                    <div className="footer-col-row1">
                        <img/>
                        <h3>Name here</h3>
                    </div>
                    {/* column4 */}
                    <div className="footer-col-row1">
                        <img/>
                        <h3>Name here</h3>
                    </div>
                </div>
                <hr className="footer-seperator"/>
                <div className="footer-content-row-2">
                    {/* row1 */}
                    <div className="footer-row-row2">
                        <a><img/></a>
                        <a><img/></a>
                    </div>
                    {/* row2 */}
                    <div className="footer-row-row2">
                        <a><img/></a>
                        <a><img/></a>
                    </div>
                    {/* row3 */}
                    <div className="footer-row-row2">
                        <a><img/></a>
                        <a><img/></a>
                    </div>
                    {/* row4 */}
                    <div className="footer-row-row2">
                        <a><img/></a>
                        <a><img/></a>
                    </div>
                </div>
            </div>
        </div>
        )
}

export default Footer;