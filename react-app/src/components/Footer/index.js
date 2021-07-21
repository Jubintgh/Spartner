import React from 'react';
import "./Footer.css";

const Footer = () => {
    return (
        <div className="main-footer">
            <div className="footer-container">
                <h3 className="footer-title">Spartner was a collaboration by:</h3>
                <div className="footer-content-row-1">
                    {/* column1 */}
                    <div className="footer-col-row1">
                        <img className="footer-profilePic" src="/images/PlaceholderProfile.png"/>
                        <h3>Austin Keumper</h3>
                    </div>
                    {/* column2 */}
                    <div className="footer-col-row1">
                        <img className="footer-profilePic" src="/images/PlaceholderProfile.png"/>
                        <h3>Jubin Taghdir</h3>
                    </div>
                    {/* column3 */}
                    <div className="footer-col-row1">
                        <img className="footer-profilePic" src="/images/PlaceholderProfile.png"/>
                        <h3>Matthew Melendez</h3>
                    </div>
                    {/* column4 */}
                    <div className="footer-col-row1">
                        <img className="footer-profilePic" src="/images/Tony.jpg"/>
                        <h3>Tony Costanza</h3>
                    </div>
                </div>
                <hr className="footer-seperator"/>
                <div className="footer-content-row-2">
                    {/* row1 */}
                    <div className="footer-row-row2">
                        <a>yo<img/></a>
                        <a>yo<img/></a>
                    </div>
                    {/* row2 */}
                    <div className="footer-row-row2">
                        <a>yo<img/></a>
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