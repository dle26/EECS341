import React from 'react';

export const DataSources = () => {
    const sources = {
        'COVID-19 Open Research Dataset': 'https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge',
        'Daily case reports': 'https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data',
        'Novel Coronavirus 2019 Dataset': 'https://www.kaggle.com/sudalairajkumar/novel-corona-virus-2019-dataset',
        'COVID-19 demographic information': 'https://www.kaggle.com/koryto/countryinfo',
        'Tweets dataset': 'https://ieee-dataport.org/open-access/corona-virus-covid-19-tweets-dataset'
    }

    return (
        <div> Data sources: &nbsp;&nbsp;
        {Object.keys(sources).map(source => (
            <span>
                <a href={sources[source]}> {source}</a> &nbsp;&nbsp;&nbsp;
            </span>
        ))} </div>
    )
}