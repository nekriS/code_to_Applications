

function out = IMG_L1NORM(image_1_)

    [x1, y1, z] = size(image_1_);
    
    sum = 0;

    for i = 1:x1
        for j = 1:y1
            for g = 1:z

                sum = sum + double(image_1_(i, j, g));

            end
        end
    end

    out = sum;

end

