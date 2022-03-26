
function love.load()
    love.window.setTitle("Neia")
    love.window.setMode(800, 600, {resizable = false})
    love.graphics.setBackgroundColor(0, 0, 0)
    love.graphics.setDefaultFilter("nearest", "nearest")
end

function love.update(dt)
end

function love.draw()
    love.graphics.setColor(255, 255, 255)
    love.graphics.print("Play", 400, 300)
    love.graphics.print("Exit", 400, 350)
    love.graphics.print("About", 400, 400)
end