BEGIN;
INSERT INTO public.usuarios(
        criado_em,
        modificado_em,
        nome,
        email,
        senha,
        nivel_acesso,
        ativo
    )
VALUES (
        now(),
        now(),
        'Administrador Padrão',
        'admin@admin.com',
        'sha256$S1EQdBPotwrJXbOl$15a234f185be9b500344ef85aff3f187fba291382f661182f0c691882d85ca49',
        0,
        true
    );
END;
COMMIT;