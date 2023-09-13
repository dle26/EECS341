import React, { Component } from 'react';
import { SelectEntity } from './components/selectEntity';
import { Attribute } from './components/attribute';
import { EnterEmail } from './components/enterEmail';
import { CovidHeader } from './components/covidHeader';
import { Query } from './components/query';
import { SelectAttribute } from './components/selectAttribute';
import { DataSources } from './components/dataSources';
import './App.css';
import { Container, Button, Navbar, Table } from 'react-bootstrap';
import { Alert, Collapse, CardBody, Card } from 'reactstrap';
import axios from 'axios';

export const userFriendlyNames = {
  /* Entities */
  'Country': 'Country',
  'COVID19_Case': 'Coronavirus cases',
  'COVID19_Measure': 'Government measures related to coronavirus',
  'COVID19_Tweet': 'Tweets about coronavirus',
  'COVID19_Paper': 'PubMed papers about coronavirus',
  'Virus_Paper': 'PubMed papers about viruses',
  'Paper_Comparison': 'Comparisons between coronavirus papers and virus papers',
  'COVID19_Paper_Comparison': 'Comparisons between coronavirus papers',
  'Virus_Paper_Comparison': 'Comparisons between virus papers',
  'Tweet_Paper_Comparison': 'Comparisons between tweets and coronavirus papers',

  /* Country */
  'name': 'Country name',
  'population': 'Total population',
  'total_tests': 'Total number of tests administered',
  'test_population': 'Total population / Total number of tests',
  'density': 'Population density (people per sq. km.)',
  'median_age': 'Median age of country',
  'urban_pop': 'Percentage of people living in a city',
  'quarantine_start_data': 'Start date of quarantine',
  'school_close_data': 'Start date of school closings',
  'hospitalbeds': 'Number of hospital beds per 1000 people',
  'smokers': 'Percentage of population that smokes',
  'sex_ratio_birth': 'Sex ratio (male to female) at birth',
  'sex_ratio_0-13': 'Sex ratio (male to female) ages 0-13',
  'sex_ratio_14-24': 'Sex ratio (male to female) ages 14-24',
  'sex_ratio_25-53': 'Sex ratio (male to female) ages 25-53',
  'sex_ratio_54-64': 'Sex ratio (male to female) ages 54-64',
  'sex_ratio_65plus': 'Sex ratio (male to female) ages 65+',
  'sexratio': 'Sex ratio (male to female) for all ages',
  'lung_disease': 'Percentage of population with lung disease',
  'lung_female': 'Male death rate from lung-related illnesses per 100,000 people',
  'lung_male': 'Female death rate from lung-related illnesses per 100,000 people',
  'gdp': 'Nominal GDP for 2019 in 1 million USD',
  'avg_temp': 'Average temperature (C) from Jan. 2020 - March 2020',
  'first_case': 'Date of the first case',

  /* COVID19_Case */
  'ID': 'ID',
  'country': 'Country',
  'year': 'Year of case reporting',
  'month': 'Month of case reporting',
  'day': 'Day of case reporting',
  'method_of_discovery': 'Method of how the case was discovered (report filed, authority notification, symptom onset)',
  'source_of_confirmation': 'Method of case confirmation (clinical care sought, exposure, report, etc)',
  'incidence_type': 'Probability of disease at onset (Probable, suspected, confirmed, or total)',
  'incidence_value': 'Numerical value of probability of disease at onset',
  'confirmation_type': 'Confirmation type (reporting, exposure, clinical care sought, etc.)',
  'confirmation_status': 'Confirmation status of case (confirmed, probable, suspected, or total of all 3)',
  'outcome': 'Outcome of case (ongoing case or death)',

  /* COVID19_Measure */
  'category': 'Category of government measure (social distancing, public health measure, lockdown, etc.)',
  'measure': 'Government measure',
  'comments': 'Comments about government measure',
  'source': 'Source of government measure',
  'implementation_year': 'Implementation year',
  'implementation_month': 'Implementation month',
  'implementation_day': 'Implementation day',

  /* COVID19_Tweet */
  'tweet_id': 'Tweet ID',
  'tweet_text': 'Tweet text',
  'tweet_year': 'Year of tweet',
  'tweet_month': 'Month of tweet',
  'tweet_day': 'Day of tweet',
  'tweet_hour': 'Hour of tweet',
  'tweet_minute': 'Minute of tweet',
  'tweet_country': 'Country of tweet',
  'username': 'Twitter handle',
  'bio': 'Twitter user bio',
  'numfollowers': 'Number of followers',
  'numretweets': 'Number of retweets',
  'sentiment_score': 'Sentiment score of tweet',

  /* COVID19_Paper */
  'title': 'Title of paper',
  'abstract': 'Abstract',
  'pubyear': 'Publication year',
  'pubmonth': 'Publication month',
  'pubday': 'Publication day',
  'journal': 'Journal',
  'authors': 'Authors',
  'countries': 'Country of paper',
  'full_text': 'Full text',
  'references': 'References',

  /* Paper_comparison */
  'covid_title': 'Title of coronavirus paper',
  'virus_title': 'Title of virus paper',
  'abstract_shared_keywords': 'Abstract shared keywords',
  'abstract_shared_bigrams': 'Abstract shared bigrams',
  'fulltext_shared_keywords': 'Full text shared keywords',
  'fulltext_shared_bigrams': 'Full text shared bigrams',

  /* COVID19_Paper_comparison */
  'covid_title1': 'Title of coronavirus paper 1',
  'covid_title2': 'Title of coronavirus paper 2',

  /* Virus_paper_comparison */
  'virus_title1': 'Title of virus paper 1',
  'virus_title2': 'Title of virus paper 2',

  /* Tweet_paper_comparison */
  'tweetid': 'Tweet ID',
  'shared_keywords': 'Shared keywords',
}

const entities = {
  'Country': ['name', 'population', 'total_tests', 'test_population', 'density', 'median_age', 'urban_pop', 'quarantine_start_data',
    'school_close_data', 'hospitalbeds', 'smokers', 'sex_ratio_birth', 'sex_ratio_0-13', 'sex_ratio_14-24', 'sex_ratio_25-53', 'sex_ratio_54-64', 'sex_ratio_65plus',
    'sexratio', 'lung_disease', 'lung_female', 'lung_male', 'gdp', 'avg_temp', 'first_case'],
  'COVID19_Case': ['ID', 'country', 'year', 'month', 'day', 'method_of_discovery', 'source_of_confirmation', 'incidence_type', 'incidence_value', 'outcome'],
  'COVID19_Measure': ['ID', 'country', 'category', 'measure', 'comments', 'source', 'implementation_year', 'implementation_month', 'implementation_day'],
  'COVID19_Tweet': ['tweet_ID', 'tweet_text', 'tweet_year', 'tweet_month', 'tweet_day', 'tweet_hour', 'tweet_minute', 'tweet_country', 'username', 'bio', 'numfollowers', 'numretweets', 'sentiment_score'],
  'COVID19_Paper': ['ID', 'title', 'abstract', 'pubyear', 'pubmonth', 'pubday', 'journal', 'authors', 'countries', 'full_text', 'references'],
  'Virus_Paper': ['ID', 'title', 'abstract', 'pubyear', 'pubmonth', 'pubday', 'journal', 'authors', 'countries', 'full_text'],
  'Paper_Comparison': ['ID', 'covid_title', 'virus_title', 'abstract_shared_keywords', 'abstract_shared_bigrams',
    'fulltext_shared_keywords', 'fulltext_shared_bigrams'],
  'COVID19_Paper_Comparison': ['ID', 'covid_title1', 'covid_title2', 'abstract_shared_keywords', 'abstract_shared_bigrams',
    'fulltext_shared_keywords', 'fulltext_shared_bigrams'],
  'Virus_Paper_Comparison': ['ID', 'virus_title1', 'virus_title2', 'abstract_shared_keywords', 'abstract_shared_bigrams',
    'fulltext_shared_keywords', 'fulltext_shared_bigrams'],
  'Tweet_Paper_Comparison': ['ID', 'covid_title', 'tweetid', 'shared_keywords']
};

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      selectedEntities: [],
      selectedAttributes: {
        'Country': [],
        'COVID19_Case': [],
        'COVID19_Measure': [],
        'COVID19_Tweet': [],
        'COVID19_Paper': [],
        'Virus_Paper': [],
        'Paper_Comparison': [],
        'COVID19_Paper_Comparison': [],
        'Virus_Paper_Comparison': [],
        'Tweet_Paper_Comparison': []
      },
      inputtedAttributes: {},
      query: '',
      result: [],
      searchCollapse: true,
      resultCollapse: false,
      email: '',
    }
  }

  refreshPage = () => {
    window.location.reload(false);
  }

  entityClicked = (entity) => {
    // callback
    const cb = () => this.formQuery()
    const index = this.state.selectedEntities.indexOf(entity);
    if (index !== -1) {
      const arr = [...this.state.selectedEntities];
      arr.splice(index, 1);
      this.setState({ selectedEntities: arr },
        () => this.formQuery())
    } else {
      this.setState({ selectedEntities: [...this.state.selectedEntities, entity] },
        () => this.formQuery())
    }
  }

  handleAttributeSelection = (entity, attributes) => {
    const selectedEntities = [...this.state.selectedEntities];
    const index = selectedEntities.indexOf(entity);
    if (attributes !== null && index === -1) {
      selectedEntities.push(entity)
    } else if (attributes === null && index !== - 1) {
      selectedEntities.splice(index, 1);
    }
    this.setState({
      selectedAttributes: {
        ...this.state.selectedAttributes,
        [entity]: attributes || []
      },
      selectedEntities
    }, () => {
      this.formQuery()
    })
  }

  handleInputChange = (event, entity, attribute) => {
    this.setState({
      inputtedAttributes: {
        ...this.state.inputtedAttributes,
        [entity + '.' + attribute]: event.target.value,
      }
    }, () => {
      this.formQuery()
    });
  }

  formQuery = () => {
    //Get attributes
    let newQuery = this.constructSelectQuery() + ' ' +
      this.constructFromQuery() + ' ' +
      this.constructWhereQuery();
    this.setState({ query: newQuery })
  }

  constructSelectQuery() {
    let selectQuery = 'SELECT '
    for (let entity in this.state.selectedAttributes) {
      if (this.state.selectedAttributes[entity] != null) {
        for (let i = 0; i < this.state.selectedAttributes[entity].length; i++) {
          const attribute = this.state.selectedAttributes[entity][i];
          selectQuery += `${entity}.${attribute.value}, `
        }
      }
    }

    return selectQuery.charAt(selectQuery.length - 2) == ',' ?
      selectQuery.substring(0, selectQuery.length - 2) :
      selectQuery;
  }

  constructFromQuery() {
    const fromQuery = this.state.selectedEntities
      .reduce((accum, entity) => accum += `${entity}, `, 'FROM ')

    return fromQuery.charAt(fromQuery.length - 2) == ',' ?
      fromQuery.substring(0, fromQuery.length - 2) :
      fromQuery;
  }

  constructWhereQuery() {
    const whereQuery = Object.entries(this.state.inputtedAttributes)
      .reduce((accum, [attr, input]) => {
        if (input.length > 0)
          accum += `${attr} = '${input}' AND `;
        return accum;
      }, 'WHERE ')

    if (whereQuery === 'WHERE ') {
      return '';
    }

    return whereQuery.substring(whereQuery.length - 4, whereQuery.length - 1) == 'AND' ?
      whereQuery.substring(0, whereQuery.length - 5) :
      whereQuery;
  }

  handleQueryChange = (e) => {
    this.setState({ query: e.target.value });
  }

  handleCollapseSearch = () => {
    this.setState({ searchCollapse: !this.state.searchCollapse })
  }

  handleEmailChange = (e) => {
    this.setState({ email: e.target.value })
  }

  handleSubmit = () => {
    axios.get('http://localhost:5000/search', {
      params: {
        query_string: this.state.query,
        email: this.state.email
      }
    }).then((response) => {
      this.setState({ result: response.data })
    }).catch((error) => { console.log(error) })
    this.setState({ searchCollapse: false, resultCollapse: !this.state.resultCollapse })
  }

  render() {
    const TableRow = ({ row }) =>
      <tr>
        {row.map(cell => <td>{cell}</td>)}
      </tr>

    const rows = this.state.result
    return (
      <div>
        <CovidHeader />
        <Container>
          <br />
          <Container className="wrapping-container">
            <Button
              variant="secondary"
              size="lg"
              onClick={this.handleCollapseSearch, this.refreshPage}> Start new query </Button>
          </Container>
          <br />
          <Container>
            <Collapse isOpen={this.state.searchCollapse}>
              <Container>
                <Alert color="secondary">
                  <h1 className="header"> Select: &nbsp;</h1>
                  Below are datasets with their associated attributes. From at least one dataset, select which attribute(s) you would like to appear in the results table.
                  </Alert>
                <div>
                  {Object.keys(entities).map(entity => (
                    <Container> {userFriendlyNames[entity]}:
                      <SelectAttribute
                        attributeOptions={entities[entity]}
                        selectedAttributes={this.state.selectedAttributes[entity]}
                        onChange={(attributes) => this.handleAttributeSelection(entity, attributes)}
                      />
                    </Container>
                  ))}
                </div>
                <Container>
                </Container>
              </Container>
              <hr />
              <Container>
                <Alert color="secondary">
                  <h1 className="header"> From: &nbsp;</h1>
                  Select which dataset(s) to use for the query. This should include the datasets of attributes that were previously selected.
                </Alert>
                <Container className="entities-container">
                  {Object.keys(entities).map(entity => (
                    <SelectEntity
                      className="entities"
                      entity={entity}
                      onClick={() => this.entityClicked(entity)}
                      selectedEntities={this.state.selectedEntities.indexOf(entity) !== -1}
                      key={entity}
                    />
                  ))}
                </Container>
              </Container><hr />
              <Container className="attributes-container">
                <Alert color="secondary">
                  <h1 className="header"> Where: &nbsp;</h1>
                  Define condition(s) that the results must satisfy.
                </Alert>
                <Container className="attributes">
                  {this.state.selectedEntities.map(entity => (
                    entities[entity].map(attribute => (
                      <Attribute
                        entity={entity}
                        attribute={attribute}
                        onChange={(event) => this.handleInputChange(event, entity, attribute)}
                        key={attribute}
                      />
                    ))
                  ))}
                </Container>
              </Container> <hr />
              <Container className="enter-query-container">
                <Query query={this.state.query} changed={this.handleQueryChange}></Query>
              </Container> <hr />
              <Container className="wrapping-container">
                <EnterEmail value={this.state.email} changed={this.handleEmailChange} />
              </Container>
            </Collapse>
          </Container>
          <Container className="wrapping-container">
            <br />
            <Button
              className="submitButton"
              variant="outline-primary"
              size="lg"
              id="resultToggler"
              onClick={this.handleSubmit}> Submit query</Button>
            <Collapse isOpen={this.state.resultCollapse} className="result-collapse">
              <br />
              <Card className="result-table" >
                <CardBody>
                  <Table hover="true">
                    <tbody>
                      {
                        rows.map(row => <TableRow row={row} />)
                      }
                    </tbody>
                  </Table>
                </CardBody>
              </Card>
            </Collapse>
            <br /><br />
          </Container>
        </Container >
        <Container className="footer">
          <Navbar fixed="bottom" bg="light">
            <DataSources />
          </Navbar>
        </Container >
      </div >
    );
  }
}

export default App;