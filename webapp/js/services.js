'use strict';

angular.module('angularFlaskServices', ['ngResource'])
	.factory('Project', function($resource) {
		return $resource('/api/project/', {}, {
			ListProjects: {
				method: 'GET',
				params: {},
				isArray: false
			},
			GetProject: {
				method: 'GET',
				url: '/api/project/:id',
				params: {},
				isArray: false
			},
			CreateProject: {
				method: 'POST',
				params: {},
				isArray: false
			},
			UpdateProject: {
				url: '/api/project/:id',
				method: 'PUT',
				params: {},
				isArray: false
			},
			DeleteProject: {
				url: '/api/project/:id',
				method: 'DELETE',
				params: {},
				isArray: false
			}
		});
	})
		.factory('WorkExperience', function($resource) {
		return $resource('/api/work_experience/', {}, {
			ListWorkExperiences: {
				method: 'GET',
				params: {},
				isArray: false
			},
			GetWorkExperience: {
				method: 'GET',
				url: '/api/work_experience/:id',
				params: {},
				isArray: false
			},
			CreateWorkExperience: {
				method: 'POST',
				params: {},
				isArray: false
			},
			UpdateWorkExperience: {
				url: '/api/work_experience/:id',
				method: 'PUT',
				params: {},
				isArray: false
			},
			DeleteWorkExperience: {
				url: '/api/work_experience/:id',
				method: 'DELETE',
				params: {},
				isArray: false
			}
		});
	})
		.factory('WorkItem', function($resource) {
		return $resource('/api/work_item/', {}, {
			ListPWorkItem: {
				method: 'GET',
				params: {},
				isArray: false
			},
			GetWorkItem: {
				method: 'GET',
				url: '/api/work_item/:id',
				params: {},
				isArray: false
			},
			CreateWorkItem: {
				method: 'POST',
				params: {},
				isArray: false
			},
			UpdateWorkItem: {
				url: '/api/work_item/:id',
				method: 'PUT',
				params: {},
				isArray: false
			},
			DeleteWorkItem: {
				url: '/api/work_item/:id',
				method: 'DELETE',
				params: {},
				isArray: false
			}
		});
	})
		.factory('Skill', function($resource) {
		return $resource('/api/skill/', {}, {
			ListSkills: {
				method: 'GET',
				params: {},
				isArray: false
			},
			GetSkill: {
				method: 'GET',
				url: '/api/skill/:id',
				params: {},
				isArray: false
			},
			CreateSkill: {
				method: 'POST',
				params: {},
				isArray: false
			},
			UpdateSkill: {
				url: '/api/skill/:id',
				method: 'PUT',
				params: {},
				isArray: false
			},
			DeleteSkill: {
				url: '/api/skill/:id',
				method: 'DELETE',
				params: {},
				isArray: false
			}
		});
	});



