import DS from 'ember-data';

export default DS.Model.extend({
	title: DS.attr(),
	image: DS.attr(),
  ingredients: DS.attr(),
  steps: DS.attr(),
	link: DS.attr(),
});
