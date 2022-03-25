
function love.load()
    love.window.setTitle("Neia")
    love.window.setMode(800, 600, {resizable = false})
    love.graphics.setBackgroundColor(0, 0, 0)
end

function love.update(dt)
    
end

function love.draw()
    love.graphics.print("Hello World!", 400, 300)
end