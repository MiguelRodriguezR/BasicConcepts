var gulp = require('gulp');
var sass = require('gulp-sass');
var uglify = require('gulp-uglify');
var connect = require('gulp-connect');
var pump = require('pump');
var concat = require('gulp-concat');

htmlSources = ['*.html'];

//gulp.task('default', defaultTask);


function defaultTask(done) {
  // place code for your default task here
  done();
}

// Most important methods of gulp object are:
//
// src where we put the name of the file we want to work with and use as an input,
// pipe will take output of the previous command as pipe it as an input for the next,
// dest writes the output of previous commands to the folder we specify

gulp.task('copy',(done)=>{
  gulp.src('index.html')
  .pipe(gulp.dest('assets'));
  done();
});

// folder/*.html - will match all the HTML files in folder
// root/**/*.html - will match all the HTML files in all the folders from root to its children

gulp.task('sass',(done)=>{
  return gulp.src('styles/*.scss')
    .pipe(sass().on('error', sass.logError))
    .pipe(gulp.dest('assets'));
    done();
});

// creando un whatcher para sass

gulp.task('sass:watch', function (done) {
  gulp.watch('styles/*.scss', gulp.parallel('sass'));
  done();
});


gulp.task('concat', function(done) {
  return gulp.src('js/*.js')
    .pipe(concat('all.js'))
    .pipe(gulp.dest('concat/'));
    done();
});

gulp.task('compress', (done) => {
  pump([
        gulp.src('concat/*.js'),
        uglify(),
        gulp.dest('assets')
    ],
    done
  );
});



//gulp.task('default', gulp.parallel('sass','copy'));


gulp.task('connect',(done)=>{
  connect.server({
   root: '.',
   livereload: true
  })
  done();
});

gulp.task('html',(done)=>{
  gulp.src(htmlSources)
  .pipe(connect.reload())
  done();
});


gulp.task('compact',gulp.series('concat', 'compress'));
gulp.task('runall',gulp.series('html','compact','sass','connect'));
gulp.task('default', gulp.parallel('runall', 'sass:watch'));
