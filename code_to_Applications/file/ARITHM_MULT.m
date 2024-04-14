

function output_image = ARITHM_MULT(image_1_, image_2_)
    [x1, y1, z] = size(image_1_);

    if string(class(image_2_)) == 'double'
        image_2_ = zeros(x1, y1, z) + image_2_;
    end

    [x2, y2, z] = size(image_2_);
    
    output_image_ = zeros(x1, y1, z);
    
    if (x1 == x2) && (y1 == y2)
        
        for i = 1:x1
            for j = 1:y1
                for g = 1:z
                    output_image_(i, j, g) = image_1_(i, j, g) * image_2_(i, j, g);

                    if output_image_(i, j, g) > 255
                        output_image_(i, j, g) = 255;
                    end


                end
            end
        end
        output_image = uint8(output_image_);
    else
        output_image = image_1_;
    end
end

