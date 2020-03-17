import Vue from 'vue'
import numeral from 'numeral'
import moment from 'moment'
import pluralize from 'pluralize'

Vue.filter('numberFormat', function(value, decimal=0) {
    return numeral(Math.round(value, decimal)).format('0,0');
});

Vue.filter('dateFormat', value => {
    return moment(value).fromNow();
});

Vue.filter('columnFormat', value => {
    return value.replace('_', ' ')
});

Vue.filter('byteFormat', value => {
    return numeral(value).format('0.0 b')
})

Vue.filter('capitalize', value => {
    if (!value) return ''
    value = value.toString()
    return value.charAt(0).toUpperCase() + value.slice(1)
})

Vue.filter('round', value => {
    return Math.round(value, 0)
})

Vue.filter('filename', value => {
    return value.split('/').slice(-1)[0]
})

Vue.filter('pluralize', function (value, number) {
    return pluralize(value, number)
})