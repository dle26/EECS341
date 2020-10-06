import React from "react";
import '../App.css';
import { Jumbotron, Container } from 'react-bootstrap';

export const CovidHeader = () => {
    return (
        <Container>
            <Jumbotron align="center">
                <h1 class="leader">COVID-19 Database Development Initiative</h1>
                Case Western Reserve University
          </Jumbotron>
        </Container>
    )
}