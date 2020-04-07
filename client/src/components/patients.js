import React from 'react';
import { List, Datagrid, TextField, Create, SimpleForm, TextInput, Edit, BooleanInput } from 'react-admin';

export const PatientList = props => (
    <List {...props} sort={{ field: 'firstName', order: 'asc' }}>
        <Datagrid rowClick="edit">
            <TextField sortable={false} source="id"/>
            <TextField source="name" />
        </Datagrid>
    </List>
);

export const PatientCreate = props => (
    <Create {...props}>
        <SimpleForm>
            <TextInput source="name" />
        </SimpleForm>
    </Create>
);

export const PatientEdit = props => (
    <Edit {...props}>
        <SimpleForm>
            <TextInput disabled source="id" />
            <TextInput source="name" />
        </SimpleForm>
    </Edit>
);

