const express = require('express')
const path    = require("path");
const app     = express()
const port    = 7969

app.get('/',
        function (req,
                  res)
        {
            const options = {
                root: path.join(__dirname)
            };

            const fileName = 'index.html';
            res.sendFile(fileName, options, function (err)
            {
                if (err)
                {
                    console.log(err);
                    res.status(err.status)
                       .end()
                }
            });
        });

app.listen(port, () => console.log(`Example app listening on port ${port}`));