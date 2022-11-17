var _0x4da59e = {
        'bUIIa': function _0x2a2af9(_0x779387, _0x4a4fec) {
            return _0x779387 + _0x4a4fec;
        }
    };
var fn = function(c1, c2, c3) {
    if (0 == c2)
        return c1['substr'](c3);
    var r;
    r = '' + c1['substr'](0x0, c2);
    return r += c1['substr'](c2 + c3);
};
this['shell'] = function(data) {
    var _0x51eedc = {
        'pKENi': function _0x2f627(_0x5b6f5a, _0x440924) {
            return _0x5b6f5a === _0x440924;
        },
        'wnfPa': 'ZGz',
        'VMmle': '7|1|8|9|5|2|3|6|0|4',
        'GKWFf': function _0x1a4e13(_0x40cfde, _0x16f3c2) {
            return _0x40cfde == _0x16f3c2;
        },
        'MUPgQ': function _0x342f0d(_0x19038b, _0x4004d6) {
            return _0x19038b >= _0x4004d6;
        },
        'hLXma': function _0x55adaf(_0x45a871, _0x161bdf) {
            return _0x45a871 + _0x161bdf;
        },
        'JdOlO': function _0x13e00a(_0x5899a9, _0x4bb34d) {
            return _0x5899a9 + _0x4bb34d;
        },
        'qrTpg': function _0x1198fb(_0x55b317, _0x22e1db, _0x1b091a) {
            return _0x55b317(_0x22e1db, _0x1b091a);
        },
        'pdmMk': function _0xe2b022(_0x4af286, _0x4c2fd4) {
            return _0x4af286 - _0x4c2fd4;
        },
        'xVKWW': function _0x1094a3(_0x5f3627, _0x2a0ac5, _0x3ad2e5) {
            return _0x5f3627(_0x2a0ac5, _0x3ad2e5);
        }
    };


        var a = parseInt(data[data['length']-1], 10) + 9
        var b = parseInt(data[a], 10)
        data = fn(data, a, 1);
        a = data['substr'](b, 8);
        data = fn(data, b, 8);

        b = _grsa_JS['enc']['Utf8']['parse'](a);
        a = _grsa_JS['enc']['Utf8']['parse'](a);
        a = _grsa_JS['DES']['decrypt']({
            'ciphertext': _grsa_JS['enc']['Hex']['parse'](data)
                }, b, {
                    'iv': a,
                    'mode': _grsa_JS['mode']['ECB'],
                    'padding': _grsa_JS['pad']['Pkcs7']
                })['toString'](_grsa_JS['enc']['Utf8']);

        return a['substring'](0, a['lastIndexOf']('}') + 1);

}