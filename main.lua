
function love.load()
    love.window.setTitle("Neia")
    love.window.setMode(800, 600, {resizable = false})
    love.graphics.setBackgroundColor(0, 0, 0)
    love.graphics.setDefaultFilter("nearest", "nearest")
    player = {
        health = 100,
        max_health = 100,
        level = 1,
        xp = 0,
        attack = 10,
        defense = 8,
        heal = 5,
        gold = 0,
        inventory = {},
    }
end

function love.update(dt)
    player.health = player.health
    if player.health <= 0 then
        player.health = 0
    end
end

function love.draw()
    love.graphics.print("Health: " .. player.health, 10, 10)
    love.graphics.print("Level: " .. player.level, 10, 30)
    love.graphics.print("XP: " .. player.xp, 10, 50)
    love.graphics.print("Attack: " .. player.attack, 10, 70)
    love.graphics.print("Defense: " .. player.defense, 10, 90)
    love.graphics.print("Heal: " .. player.heal, 10, 110)
    love.graphics.print("Gold: " .. player.gold, 10, 130)
    love.graphics.rectangle("fill", 10, 150, player.health / player.max_health * 100, 20)
    if player.health == 0 then
        love.graphics.print("You died!", 50, 170 , 0, 2, 2 )
    end
end