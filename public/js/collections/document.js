'use strict';

var app = app || {};

app.DocumentCollection = Backbone.Collection.extend({
  model: app.Document,
  url: '/api/documents'
});

