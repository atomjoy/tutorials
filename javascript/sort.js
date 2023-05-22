function compare(a, b) {
    if (a < b) {
        return -1
    }
    if (a > b) {
        return 1
    }
    return 0
}

function compareNr(a, b) {
    return a - b
}

tab.sort(compare);

tab.sort(function(a, b) {
    return a.height - b.height;
});

users.sort(function(a, b) {
    return a.cat.age - b.cat.age
});

