import React from 'react';
import {IconContext} from 'react-icons';
import {FaLinkedin, FaGithub} from 'react-icons/fa';
import "./Footer.css";

const Footer = () => {
    return (
        <div className="main-footer">
            <div className="footer-container">
                <h3 className="footer-title">Spartner was a collaboration by:</h3>
                <div className="footer-content-row-1">
                    {/* column1 */}
                    <div className="footer-col-row1">
                        <img className="footer-profilePic" src="/images/Austin.jpg"/>
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
                <IconContext.Provider value={{ className: 'react-icons'}}>
                <div className="footer-content-row-2">
                    {/* row1 */}
                    <div className="footer-row-row2">
                        <a href="https://github.com/AKuemper" target="_blank"><FaGithub/></a>
                        <a href="https://www.linkedin.com/in/austin-kuemper-0b471b84/" target="_blank"><FaLinkedin/></a>
                    </div>
                    {/* row2 */}
                    <div className="footer-row-row2">
                        <a href="https://github.com/Jubintgh" target="_blank"><FaGithub/></a>
                        <a href="https://www.linkedin.com/in/jubintaghdir/" target="_blank"><FaLinkedin/></a>
                    </div>
                    {/* row3 */}
                    <div className="footer-row-row2">
                        <a href="https://github.com/melendezmatt" target="_blank"><FaGithub/></a>
                        <a href="https://www.linkedin.com/in/matthew-melendez/" target="_blank"><FaLinkedin/></a>
                    </div>
                    {/* row4 */}
                    <div className="footer-row-row2">
                        <a href="https://github.com/AnthonyCost" target="_blank"><FaGithub/></a>
                        <a href="https://www.linkedin.com/in/anthony-costanza-64952820a/" target="_blank"><FaLinkedin/></a>
                    </div>
                </div>
                    </IconContext.Provider>
            </div>
        </div>
        )
}

export default Footer;