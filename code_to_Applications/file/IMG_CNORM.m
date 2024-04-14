

function out = IMG_CNORM(image_1_)

    [x1, y1, z] = size(image_1_);
    
    max = -1;

    for i = 1:x1
        for j = 1:y1
            for g = 1:z
                if image_1_(i, j, g) > max
                    max = image_1_(i, j, g);
                end
            end
        end
    end

    out = max;

end

