import jQuery from './vendor/jquery';
import pluralize from './vendor/pluralize';

// We have to manually make jQuery a global variable.
// By default it will be in a closure and renamed to lowercase.
window.jQuery = jQuery;

// Promise polyfill for older browsers
import Promise from './vendor/promise';
if (!window.Promise) {
    window.Promise = Promise;
}

// fetch polyfill
import './vendor/fetch';

export { pluralize, jQuery };
export default jQuery;
