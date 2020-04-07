import React, { Component } from 'react';
import buildGraphQLProvider from 'ra-data-graphql-simple';
import { Admin, Resource } from 'react-admin';

import { PatientList, PatientCreate, PatientEdit } from './components/patients';

console.log(process.env.REACT_APP_API_ENTRYPOINT);

class App extends Component {
    constructor() {
        super();
        this.state = { dataProvider: null };
    }
    componentDidMount() {
        buildGraphQLProvider({ clientOptions: { uri: 'http://localhost:8000/graphql' }})
            .then(dataProvider => this.setState({ dataProvider }));
    }

    render() {
        const { dataProvider } = this.state;

        if (!dataProvider) {
            return <div>Loading</div>;
        }

        return (
            <Admin dataProvider={dataProvider}>
                <Resource name="Patient" list={PatientList} edit={PatientEdit} create={PatientCreate} />
            </Admin>
        );
    }
}

export default App;