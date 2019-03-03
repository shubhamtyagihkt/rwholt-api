var express = require('express');
var router = express.Router();
var PythonShell = require('python-shell').PythonShell;

/* GET home page. */


router.get('/possible-locations', function(req, res) {
    var options = {
        args:
            [
                req.query.funds, // starting funds
                req.query.size, // (initial) wager size
                req.query.count, // wager count — number of wagers per sim
                req.query.sims // number of simulation
            ]
    };
    PythonShell.run('ml-python/json_parser.py', options, function (err, data) {
        if (err) res.send(err);
        res.send(data.toString());
    });
});

router.get('/locations', function(req, res) {
    var options = {
        args:
            [
                req.query.funds, // starting funds
                req.query.size, // (initial) wager size
                req.query.count, // wager count — number of wagers per sim
                req.query.sims // number of simulation
            ]
    };
    PythonShell.run('ml-python/possible_locations.py', options, function (err, data) {
        if (err) res.send(err);
        res.send(data.toString());
    });
});

router.get('/cost-estimation', function(req, res) {
    var options = {
        args:
            [
                req.query.funds, // starting funds
                req.query.size, // (initial) wager size
                req.query.count, // wager count — number of wagers per sim
                req.query.sims // number of simulation
            ]
    };
    PythonShell.run('ml-python/CALCULATING_THE_COST_OF_SETUP.py', options, function (err, data) {
        if (err) res.send(err);
        res.send(data);
    });
});
module.exports = router;
