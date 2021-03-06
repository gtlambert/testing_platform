'use strict';

var gulp = require('gulp'),
	sass = require('gulp-sass'),
	maps = require('gulp-sourcemaps'),
	del = require('del'),
	uglify = require('gulp-uglify'),
	concat = require('gulp-concat');

gulp.task('compileSass', function() {
	return gulp.src('static/scss/main.scss')
		.pipe(maps.init())
		.pipe(sass())
		.pipe(maps.write('./'))
		.pipe(gulp.dest('static/css'));
});

gulp.task('watchFiles', function() {
	gulp.watch('static/scss/*.scss', ['compileSass']);
});

gulp.task('clean', function() {
	del('static/css/main.css');
})

// gulp.task('compress', function() {
// 	return gulp.src('static/js/*.js')
// 		.pipe(uglify())
// 		.pipe(gulp.dest('static/js/min'));
// });

// gulp.task('concatenation', function() {
// 	return gulp.src(['static/js/min/*.js'])
// 		.pipe(concat('all.js'))
// 		.pipe(gulp.dest('static/js/'));
// })

gulp.task('default', ['clean', 'compileSass'], function() {
	gulp.start('watchFiles');
});