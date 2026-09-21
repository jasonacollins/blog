local function ensureHtmlDeps()
    quarto.doc.addHtmlDependency({
        name = 'twitter',
        version = '0.0.1',
        scripts = {
            { 
                path = "",
                attribs = {src="https://platform.twitter.com/widgets.js"},
                afterBody = true
            }
        }
    })
end
   
local function isEmpty(s)
    return s == nil or s == ''
end

function tweet(args, kwargs)
    if quarto.doc.isFormat('html') then
        ensureHtmlDeps()

        local user, status_id
        if isEmpty(args[1]) then
            user = pandoc.utils.stringify(kwargs["user"])
            status_id = pandoc.utils.stringify(kwargs["id"])
        else
            user = pandoc.utils.stringify(args[1])
            status_id = pandoc.utils.stringify(args[2])
        end

        -- Let widgets.js load the tweet in the browser. Build-time oEmbed
        -- requests can fail for deleted tweets or an unavailable X service.
        local function escapeHtml(value)
            return (value:gsub('&', '&amp;'):gsub('<', '&lt;')
                :gsub('>', '&gt;'):gsub('"', '&quot;'):gsub("'", '&#39;'))
        end
        local url = 'https://twitter.com/' .. user .. '/status/' .. status_id
        local tweet_data = '<blockquote class="twitter-tweet" data-align="center">'
            .. '<a href="' .. escapeHtml(url) .. '">View tweet by @'
            .. escapeHtml(user) .. '</a></blockquote>'

        return pandoc.RawInline('html', tweet_data)
    else
        return pandoc.Null()
    end
end
